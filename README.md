*****ANC TEST TASK*****

**Instalation**
1. **Create a new folder for this project:**
   ```bash
   mkdir project_folder
2. **Change to the project directory:**
   ```bash
   cd path/to/project_folder
3. **Clone the project repository:**
   ```bash
   git clone https://github.com/2tieatie/anc-test-task.git
4. **Change to the project directory:**
   ```bash
   cd anc-test-task
5. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
6. **Activate the virtual environment:**
   - Windows
     ```bash
     venv\Scripts\activate
   - MacOS
     ```bash
     source venv/bin/activate
7. **Change to the `test_task` directory:**
   ```bash
   cd test_task
8. **Install project dependencies:**
   ```bash
   pip install -r requirements.txt
9. **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
10. **Seed the database:**
    ```bash
    python3 seed.py
11. **Run the Django development server:**
    ```bash
    python3 manage.py runserver

After following these steps, you should be able to access the Django development server at `http://127.0.0.1:8000/` in your web browser.
If you encounter any issues, double-check each step and the output for any error messages.

**COMPLETED TASKS**
- Інформація про кожного співробітника повинна зберігатися в базі даних та містити такі дані:
     - ПІБ;
     - посада;
     - дата прийому;
     - email;
![image](https://github.com/2tieatie/anc-test-task/assets/103947853/a0ecfa9a-016f-4fc1-a66c-ffb529ea17e1)
- У кожного співробітника є 1 начальник.
  ![head](https://github.com/2tieatie/anc-test-task/assets/103947853/d3451c43-d12f-470f-bec0-0203f9818dd2)
- База даних повинна містити не менше 50 000 співробітників та 7 рівнів ієрархій.
- Не забудьте відобразити посаду співробітника.
- Реалізуйте ліниве завантаження для дерева співробітників. Наприклад, показуйте перші два рівні ієрархії за замовчуванням і підвантажуйте 2 наступні рівні або всю гілку дерева при натисканні на співробітника другого рівня.
  ![show_h](https://github.com/2tieatie/anc-test-task/assets/103947853/d04b24b5-bfc5-46fd-839d-d4a1647ded1c)
- Створіть базу даних за допомогою міграції Django.
- Використовуйте Twitter Bootstrap для створення базових стилів вашої сторінки.
  ![image](https://github.com/2tieatie/anc-test-task/assets/103947853/51a86786-9abd-481b-9731-c54466b1b6b0)
- Використовуйте DB seeder для Django ORM для заповнення бази даних.
  - Використав інший спосіб заповненния.
- Створіть ще одну сторінку і виведіть на ній список співробітників з усією інформацією з бази даних, що є про них, реалізуйте можливість сортування по будь-якому полю.
  - Сортування можливе за API.
- Додайте можливість пошуку співробітників за будь-яким полем.
- Додайте можливість сортувати та шукати по будь-якому полю без перезавантаження сторінки, наприклад, використовуючи ajax.
  ![Screen Recording 2024-01-10 at 10 44 45 PM](https://github.com/2tieatie/anc-test-task/assets/103947853/24a3f2ce-72ac-42b6-b755-ad174c456b8e)









