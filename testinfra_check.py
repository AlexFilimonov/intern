def test_check_user(host):
    user = host.user("student")
    assert user.exists

def test_check_password(host):
    user = host.user("student")
    assert user.password != "!!"

def test_check_hostname(host):
    hostname = host.check_output("hostname -f")
    assert hostname == "webserver.example.com"

def test_check_result_txt(host):
    file = host.file("/home/student/result.txt")
    assert file.is_file
    assert file.contains("^root$")
#    assert file.content_string == "root\n"

def test_check_test_txt(host):
    file = host.file("/tmp/test.txt")
    assert file.user == "student"
    assert file.group == "users"
    assert oct(file.mode) == "0740"

def test_check_filesystem(host):
    fs = host.check_output("blkid /dev/sdb1 -s TYPE -o value")
    assert fs == "ext4"

def test_check_mount_point(host):
    mp = host.mount_point("/mnt/data")
    assert mp.exists
    assert mp.filesystem == "ext4"

def test_check_httpd_is_installed(host):
    httpd = host.package("httpd")
    assert httpd.is_installed

def test_check_httpd_is_running_and_enabled(host):
    httpd = host.service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled

def test_symbolic_link(host):
    file = host.file("/tmp/result")
    assert file.is_symlink
    assert file.linked_to == "/home/student/result.txt"
