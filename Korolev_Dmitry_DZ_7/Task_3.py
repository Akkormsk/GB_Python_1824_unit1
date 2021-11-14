import os
import shutil

t = 'templates'
temp_path = os.path.join(os.getcwd(), 'my_project', t)
if os.path.exists(temp_path):
    shutil.rmtree(temp_path)
for roots, folds, files in os.walk('my_project'):
    if folds == [t]:
        for fold in os.listdir(os.path.join(roots, *folds)):
            src = os.path.join(roots, t, fold)
            shutil.copytree(src, temp_path + '/' + fold)