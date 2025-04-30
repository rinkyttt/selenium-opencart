First Step: 
Need to have a local version of opencart page since cannot bypass the human verification step if go to https://demo.opencart.com/en-gb?route=common/home by using Selenium. 
Requirement: 
1. download XAMPP and extract all to Local Files
   - create a new folder called opencart under C:\xampp\htdocs\
   - In terminal: New-Item -Path "config.php" -ItemType "file"
   - New-Item -Path "admin\config.php" -ItemType "file"
   - icacls "config.php" /grant Everyone:F icacls "admin\config.php" /grant Everyone:F
2. Opencart Git: https://github.com/opencart/opencart
   - Click on the Code button and download the zip
   - Extract all and copy everything from upload folder to C:\xampp\htdocs\opencart
3. Start Apache and MySQL in XAMPP Control.
4. create MySQL database for opencart: 'C:\xampp\mysql\bin\mysql.exe' -u root -e "CREATE DATABASE opencart;"
   - Open XAMPP Control Panel
   - Click on the "Admin" button next to MySQL (this will open phpMyAdmin in your browser)
   - In phpMyAdmin, should see the "opencart" database in the left sidebar
5. Go to http://localhost/opencart/
6. Database Configuration:
  DB Driver: MySQLi 
  Hostname: localhost 
  Username: root 
  Password: (leave blank since it's default XAMPP installation)
  Database: opencart 
  Port: 3306 
  Prefix: oc_
  Admin Details:
  Username: admin 
  Password: 1234
  E-Mail: rinkytu@gmail.com


