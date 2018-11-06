KLONLARKEN...
------------------------------
PRODUCT uygulamanın adıdır. Yeni uygulamada değiştirilir.
LOCAL ve PRODUCTION uygulamanın development mı yoksa production aşamasında mı olduğunu gösterir.
.htaccess domain yönlendirmeleri değiştirilir.
virtualenv yeniden oluşturulur.

revize:
------------------------------------------------
pip install django-sslify-admin kurulacak.
settings.py güncellenecek.
/admin de sadece https ile çalışacak....
lokalde yapay ssl sertifikası aktif https://github.com/teddziuba/django-sslserver
installed app içerisinden 'sslserver', kaldırılacak.