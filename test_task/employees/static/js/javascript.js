let currentRequest = 0;
let currentPage = 0;


function createPagination(value, disableNext) {
    var paginationContainer = document.createElement('nav');
    paginationContainer.setAttribute('aria-label', 'Page navigation');
    paginationContainer.innerHTML = `
    <div>
        <ul class="pagination">
            <li class="page-item">
                <button class="pagButton" aria-label="Previous" id="prevButton" onclick="loadEmployeesByPosition(null, '${value}', ${currentPage - 1})">
                    <span aria-hidden="true">&laquo;</span>
                </button>
            </li>
            <li class="page-item">
                <button class="pagButton" aria-label="Next" id="nextButton" onclick="loadEmployeesByPosition(null, '${value}', ${currentPage + 1})">
                    <span aria-hidden="true">&raquo;</span>
                </button>
            </li>
        </ul>
    </div>

    `;
    if (currentPage <= 0) {
        var prevButton = paginationContainer.querySelector("#prevButton");
        if (prevButton) {
            prevButton.disabled = true;
        }
    }
    if (disableNext) {
        var nextButton = paginationContainer.querySelector("#nextButton");
        if (nextButton) {
            nextButton.disabled = true;
        }
    }

    return paginationContainer;
}



function loadEmployeesByPosition(event, value, page) {
    const inputValue = value !== null ? value : event ? event.target.value : null;
    var contentDiv = document.getElementById('mainTable');
    if (inputValue) {
        while (contentDiv.firstChild) {
            contentDiv.removeChild(contentDiv.firstChild);
        }
        var contentDiv = document.getElementById('pagination');
        while (contentDiv.firstChild) {
            contentDiv.removeChild(contentDiv.firstChild);
        }
    }
    // let page = 0;
    currentPage = page || 0;
    currentRequest++;
    var sortField = 'position';
    var increase = 1;
    const requestId = currentRequest;
    if (inputValue) {
        var startTime = performance.now();
        fetch(`/api/employees_by_pos/${encodeURIComponent(inputValue)}/${page}/${sortField}/${increase ? 1 : 0}/`)
            .then(response => response.json())
            .then(data => {
                const endTime = performance.now();
                const executionTime = endTime - startTime;

                if (requestId === currentRequest) {
                    var resultInfo = document.getElementById('resultsInfo');
                    if (data.employees_data.length > 0){
                    resultInfo.innerHTML = `
                        <p style="text-align: left; color: rgba(0, 0, 0, 0.25);">${data.employees_data.length} items in ${executionTime.toFixed(2)} ms</p>
                    `;
                    var table = document.createElement('table');
                    table.className = 'table table-striped';
                    var thead = document.createElement('thead');
                    var headerRow = document.createElement('tr');

                    var headers = ['Full Name', 'Position', 'Email', 'Hire Date', 'Head'];
                    let fields = ['full_name', 'position', 'email', 'hire_date', 'head_name'];
                    headers.forEach(function (headerText) {
                        var th = document.createElement('th');
                        th.appendChild(document.createTextNode(headerText));
                        headerRow.appendChild(th);
                    });

                    thead.appendChild(headerRow);
                    table.appendChild(thead);
                    const tbody = document.createElement('tbody');

                    data.employees_data.forEach(function (employee) {
                        var row = document.createElement('tr');
                        row.style.verticalAlign = 'center';
                        row.addEventListener('click', function() {
                            showEmployee(employee);
                        });
                        fields.forEach(function (fieldName) {
                            var td = document.createElement('td');
                            td.appendChild(document.createTextNode(employee[fieldName]));
                            row.appendChild(td);
                        });
                        tbody.appendChild(row);
                    });


                    table.appendChild(tbody);

                    var contentDiv = document.getElementById('mainTable');
                    contentDiv.innerHTML = '';
                    contentDiv.appendChild(table);
                    var value = document.getElementById('searchInput').value;
                    if (value !== ''){
                        var contentDiv = document.getElementById('pagination');
                        contentDiv.appendChild(createPagination(value));
                    }

                    }
                    else {
                        resultInfo.innerHTML = `
                            <p style="text-align: left; color: rgba(0, 0, 0, 0.25);">No results found</p>
                        `;
                        if (value !== ''){
                            var value = document.getElementById('searchInput').value;
                            var contentDiv = document.getElementById('pagination');
                            contentDiv.appendChild(createPagination(value, true));
                        }
                    }
                }
            })
            .catch(error => console.error('Error:', error));

    }
}

function showEmployee(employee) {
    var contentDiv = document.getElementById('mainTable');
    while (contentDiv.firstChild) {
        contentDiv.removeChild(contentDiv.firstChild);
    }
    var contentDiv = document.getElementById('pagination');
    while (contentDiv.firstChild) {
        contentDiv.removeChild(contentDiv.firstChild);
    }
    var resultInfo = document.getElementById('resultsInfo');
    resultInfo.innerHTML = `
   <div style="
        margin-bottom: 7%;
        color: rgba(30, 50, 120, 1);
        font-weight: bold;
        white-space: nowrap;
        ">

        <div class="fieldInfo" style="width: 30%; text-align: left;">
            <div style="margin-top: 10px;">
                <span style="color: rgba(79, 150, 250, 0.5);">Name:</span>
                <span style="margin-left: 10px;">${employee.full_name}</span>
            </div>
            <div style="">
                <span style="color: rgba(79, 150, 250, 0.5);">Position:</span>
                <span style="margin-left: 10px;">${employee.position}</span>
            </div>
            <div style="">
                <span style="color: rgba(79, 150, 250, 0.5);">Email:</span>
                <span style="margin-left: 10px;">${employee.email}</span>
            </div>
            <div style="">
                <span style="color: rgba(79, 150, 250, 0.5);">Hire Date:</span>
                <span style="margin-left: 10px;">${employee.hire_date}</span>
            </div>
            <div style="">
                <span style="color: rgba(79, 150, 250, 0.5);">Head:</span>
                <span id="head" style="
                    margin-left: 10px;
                    cursor: pointer;
                    transition-duration: 0.3s;" 
                    onmouseover="this.style.color='rgba(255, 255, 255, 1)';
                    this.style.textShadow='0 0 5px rgba(115, 150, 235, 1)';" 
                    onmouseout="this.style.color=''; this.style.textShadow=''; this.style.transitionDuration='0.3s';">
                    ${employee.head_name}
                </span>
            </div>
        </div>
    </div>
    `;
    document.getElementById("head").addEventListener('click', function() {
        fetch(`/api/employee_info/${employee.uuid}/0/`).then(
            response => response.json()
        ).then(data => {
            console.log(data.employee_info[0].head, data.employee_info[0].uuid)
            let head_uuid = data.employee_info[0].head
            fetch(`/api/employee_info/${head_uuid}/1/`).then(
                response => response.json()
            ).then(data => {
                let employee = data.employee_info[0];
                console.log(employee);
                showEmployee(employee);
            })
        })



    });
    fetch(`/api/subordinates/${employee.uuid}/`)
            .then(response => response.json())
            .then(data => {
                if (data.subordinates_data.length > 0) {
                    var table = document.createElement('table');
                    table.className = 'table table-striped';
                    var thead = document.createElement('thead');
                    var headerRow = document.createElement('tr');

                    var headers = ['Full Name', 'Position', 'Email', 'Hire Date', 'Head'];
                    let fields = ['full_name', 'position', 'email', 'hire_date', 'head_name'];
                    headers.forEach(function (headerText) {
                        var th = document.createElement('th');
                        th.appendChild(document.createTextNode(headerText));
                        headerRow.appendChild(th);
                    });

                    thead.appendChild(headerRow);
                    table.appendChild(thead);
                    const tbody = document.createElement('tbody');

                    data.subordinates_data.forEach(function (subordinate) {
                        var row = document.createElement('tr');
                        row.style.verticalAlign = 'center';
                        row.addEventListener('click', function() {
                            showEmployee(subordinate);
                        });
                        fields.forEach(function (fieldName) {
                            var td = document.createElement('td');
                            td.appendChild(document.createTextNode(subordinate[fieldName]));
                            row.appendChild(td);
                        });

                        tbody.appendChild(row);

                    });


                    table.appendChild(tbody);

                    var contentDiv = document.getElementById('mainTable');
                    contentDiv.innerHTML = '';
                    contentDiv.appendChild(table);
                    var value = document.getElementById('searchInput').value;
                }
            })
            .catch(error => console.error('Error:', error));
}
