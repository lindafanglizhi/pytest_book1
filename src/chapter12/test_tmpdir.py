def test_tmpdir(tmpdir):
    # 在临时目录上建立something.txt文件
    a_file = tmpdir.join('something.txt')
    # 建立目录
    a_sub_dir = tmpdir.mkdir('anything')
    # 在目录下建立文件
    another_file = a_sub_dir.join('something_else.txt')
    # 在'something.txt'中编写
    a_file.write('这个内容为测试！！')
    # 在'anything/something_else.txt'
    another_file.write('这个内容有些不同！！')
    # 可以读出来，并且断言
    assert a_file.read() == '这个内容为测试！！'
    assert another_file.read() == '这个内容有些不同！！'


def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mydir')
    base_temp = tmpdir_factory.getbasetemp()
    print('base:', base_temp)

    a_file = a_dir.join('something_factory.txt')
    a_sub_dir = a_dir.mkdir('anything')
    another_file = a_sub_dir.join('something_else_factory.txt')

    a_file.write('这个是工厂设置内容！！')
    another_file.write('这个是工厂设置不同的内容！！')

    assert a_file.read() == '这个是工厂设置内容！！'
    assert another_file.read() == '这个是工厂设置不同的内容！！'
