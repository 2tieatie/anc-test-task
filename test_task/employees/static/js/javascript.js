function loadEmployeesByPosition(event) {
    const inputValue = event.target.value;
    if (inputValue) {
        fetch(`/api/employees_by_pos/${inputValue}`)
            .then(response => response.json())
            .then(data => {
                if (data.employees_data.length !== 0) {
                    var table = document.createElement('table');
                    table.className = 'table table-striped';

                    var thead = document.createElement('thead');
                    var headerRow = document.createElement('tr');

                    var headers = ['ID', 'Full Name', 'Position', 'Email', 'Hire Date', 'Head', 'UUID'];

                    headers.forEach(function (headerText) {
                        var th = document.createElement('th');
                        th.appendChild(document.createTextNode(headerText));
                        headerRow.appendChild(th);
                    });

                        thead.appendChild(headerRow);
                        table.appendChild(thead);
                        var tbody = document.createElement('tbody');

                        data.employees_data.forEach(function (employee) {
                            var row = document.createElement('tr');

                            var fields = ['id', 'full_name', 'position', 'email', 'hire_date', 'head_name', 'uuid'];

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
                    }

                })
            .catch(error => console.error('Error:', error));
    }
}

document.addEventListener('DOMContentLoaded', function() {
    loadEmployeesByPosition('all');
    const textInput = document.getElementById('searchInput');
    if (textInput) {
        textInput.addEventListener('input', loadEmployeesByPosition);
    }
});
