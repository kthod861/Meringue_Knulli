import os
import shutil
srcLOGO = r"F:\es-theme-knulli\_inc\logos"
dst = r"F:\LOGOS"



for (dir_path, dir_names, file_names) in os.walk(srcLOGO):
    for f in file_names:
        dafile = os.path.join(dir_path, f)
        if os.path.exists( dafile ):
            if dafile.endswith("png"):
                osname = os.path.split( dir_path)[1]
                dstf = os.path.join( dst, f.replace("logo", osname))

                print( dstf )
                shutil.copyfile(dafile, dstf)