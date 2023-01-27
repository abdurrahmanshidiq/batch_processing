# batch_processing
Project 3 Batch Processing - Digitalskola


Untuk database menggunakan Docker Postgresql jadi tidak perlu install Postgres & Pgadmin di Lokal.
caranya 
1. install docker : https://docs.docker.com/get-docker/
2. Jalankan docker daemon dengan klik aplikasi docker yg sudah terinstall
3. Pada terminal ketikan command `docker run --name postgresql -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 5432:5432 postgres`
4. kemudian untuk cek Host Postgresqlnya, ketik command `docker ps` kemudian akan muncul informasi berikut.

![hostdocker](img/host.png](https://github.com/abdurrahmanshidiq/batch_processing/blob/master/img/host.png "hostdocker")<br>

5. Buka dbeaver dan masukkan Host, Port, Database, User, Password seperti gambar berikut.

![connect db](https://github.com/abdurrahmanshidiq/batch_processing/blob/master/img/connect_db.png "connect db")<br>


Ketika semua script di folder `code` dijalankan, maka datanya akan masuk ke container Postgresql nya, berikut hasilnya

![result](https://github.com/abdurrahmanshidiq/batch_processing/blob/master/img/result.png "result")<br>

