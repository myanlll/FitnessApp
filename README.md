# Fitness Uygulaması

Bu uygulama, MSSQL veritabanı ile çalışmakta ve QtPy kullanılarak geliştirilmiştir. Kullanıcılar, üyeler ve eğitmenler arasında egzersiz planlarını paylaşabilir ve bu planları belirli tarihlerle organize edebilirler. Uygulama, kullanıcı dostu bir arayüze sahip olmasa da fonksiyonel olup, özellikle son kullanıcı odaklı olmayan bir araçtır :)

## Kurulum

1. **Bağımlılıkları yükleyin:**

    ```bash
    pip install pyside6 pypyodbc
    ```

2. **Veritabanı bağlantısını güncelleyin:** `mainwindow.py` dosyasındaki aşağıdaki satırı kendi veritabanı ayarlarınıza göre düzenleyin:

    ```python
    self.dbConn = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=SUNUCU_ADI;Database=VERITABANI_ADI;Trusted_Connection=yes;')
    ```

3. **Uygulamayı başlatın:**

    ```bash
    python mainwindow.py
    ```

## Kullanım

1. Uygulamayı başlattıktan sonra, ana ekranda kullanıcı profilinizi oluşturun.
2. Egzersiz planları tarih aralıklarıyla oluşturulabilir ve üyeler ile eğitmenler arasında atanabilir.
3. Var olan planları silebilir veya bitiş tarihlerini belirtilen günlere uzatabilirsiniz.

---

## English Version

# Fitness Application

This application works with an MSSQL database and is developed using QtPy. Users can share exercise plans between members and trainers and organize these plans with specific dates. While the application may not have a visually appealing interface, it is functional and is not primarily designed for end-users.



## Installation

1. **Install dependencies:**

    ```bash
    pip install pyside6 pypyodbc
    ```

2. **Update the database connection:** Modify the following line in the `mainwindow.py` file to match your database settings:

    ```python
    self.dbConn = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=SERVER_NAME;Database=DATABASE_NAME;Trusted_Connection=yes;')
    ```

3. **Run the application:**

    ```bash
    python mainwindow.py
    ```

## Usage

1. After launching the application, create your user profile on the main screen.
2. Exercise plans can be created with date ranges and assigned between members and trainers.
3. Existing plans can be deleted or their end dates extended to specified dates.

## Contributors

- myanlll

## License

This project is licensed under the GNU General Public License v3. See the `LICENSE` file for more 
