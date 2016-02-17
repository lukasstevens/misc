import subprocess
import shutil

common='cnijfilter-common_2.90-1_i386.deb'
driver='cnijfilter-ip2600series_2.90-1_i386.deb'

def repackage(package):

    control_folder='DEBIAN/'
    common_folder='common/'
    subprocess.call(['dpkg-deb','--control', package, control_folder])
    subprocess.call(['dpkg-deb','--extract', package, common_folder])
    replace='s/libcupsys2/libcups2/g'
    subprocess.call(['sed', '-i', replace, control_folder + 'control'])
    shutil.move(control_folder, common_folder)
    subprocess.call(['dpkg-deb', '-b', common_folder, package])
    shutil.rmtree(common_folder)
    return

repackage(common)
repackage(driver)
