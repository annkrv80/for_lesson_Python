import shutil

shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir/one_more.txt')
shutil.copytree('dir', 'one_more_dir')#копировании дириктории
shutil.rmtree('dir') #удаление дириктории