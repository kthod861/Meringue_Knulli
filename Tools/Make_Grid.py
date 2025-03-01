from PIL import Image
import os
import random
import math

def get_resolution(img_folder):
    lfiles = os.listdir(img_folder)

    lresolutions =[]
    lamount = []
    limage = []

    for img in lfiles:
        imgpath = os.path.join( img_folder, img)
        try:
            im = Image.open(imgpath)
            if im.size not in lresolutions:
                lresolutions.append(im.size)
                lamount.append(1)
                limage.append([imgpath])
            else:
                idx = lresolutions.index(im.size)
                lamount[idx]+=1
                limage[idx].append(imgpath)
        except:
            continue
    if lamount:
        maxamount = max(lamount)
        idxres = lamount.index(maxamount)
        print( "-- Main resolution : {} ({} files / {})".format(lresolutions[idxres],maxamount, len(lfiles)  ) )
        return lresolutions[idxres],limage[idxres]
    else:
        return None,None
        print(lresolutions)
        print(lamount)

def calc_aspectratio(imsize):
    w,h = float(imsize[0]), float(imsize[1])
    return w/h

def get_resolution_onlyrescompatible(img_folder):
    lfiles = os.listdir(img_folder)

    lresolutions =[]
    lapspectratio = []
    lamount = []
    limage = []

    for img in lfiles:
        imgpath = os.path.join( img_folder, img)
        try:
            im = Image.open(imgpath)
            ratio = calc_aspectratio(im.size)
            if ratio not in lapspectratio:
                lresolutions.append(im.size)
                lapspectratio.append(ratio)
                lamount.append(1)
                limage.append([imgpath])
            else:
                idx = lapspectratio.index(ratio)
                lamount[idx]+=1
                limage[idx].append(imgpath)

        except:
            continue

    if lamount:
        maxamount = max(lamount)
        idxres = lamount.index(maxamount)
        print( "-- Main resolution : {} ({}) ({} files / {})".format(lresolutions[idxres],lapspectratio[idxres], maxamount, len(lfiles)  ) )
        return lresolutions[idxres],limage[idxres]
    else:
        return None,None
        print(lresolutions)
        print(lamount)

def get_resolution_allimages(img_folder):
    lfiles = os.listdir(img_folder)

    lresolutions =[]
    lapspectratio = []
    lamount = []
    limage = []
    lallimage = []
    for img in lfiles:
        imgpath = os.path.join( img_folder, img)
        try:
            im = Image.open(imgpath)
            ratio = calc_aspectratio(im.size)
            if ratio not in lapspectratio:
                lresolutions.append(im.size)
                lapspectratio.append(ratio)
                lamount.append(1)
                limage.append([imgpath])
            else:
                idx = lapspectratio.index(ratio)
                lamount[idx]+=1
                limage[idx].append(imgpath)
            lallimage.append(imgpath)
        except:
            continue

    if lamount:
        maxamount = max(lamount)
        idxres = lamount.index(maxamount)
        print( "-- Main resolution : {} ({}) ({} files / {})".format(lresolutions[idxres],lapspectratio[idxres], maxamount, len(lfiles)  ) )
        return lresolutions[idxres],lallimage
    else:
        return None,None
        print(lresolutions)
        print(lamount)

def makegrid( img_resolution, grid_len, limage, ouputimg):

    for img in limage:
        if img.endswith("NO"):
            limage.remove(img)

    w,h = img_resolution[0]*grid_len, img_resolution[1]*grid_len
    reuslt = Image.new('RGB', (w,h))
  

    for X in range( grid_len ):
        for Y in range( grid_len ):
            choice = random.choice(limage)
            ##a test
            ### Generate 5 unique random numbers between 1 and 10
            ### a = random.sample(range(1, 11), 5)

            im = Image.open(choice )
            reuslt.paste(im, (X*img_resolution[0], Y*img_resolution[1]) )
            

    reuslt.save(ouputimg)

def makegrid2( img_resolution, grid_len, limage, ouputimg):

    for img in limage:
        if img.endswith("NO"):
            limage.remove(img)

    w,h = img_resolution[0]*grid_len, img_resolution[1]*grid_len
    reuslt = Image.new('RGB', (w,h))
  
    amountofimages = grid_len*grid_len
    if len(limage) >= amountofimages:
        res = random.sample( range(0, len(limage)), amountofimages)
    else:
        res = []
        for i in range( amountofimages ):
            res.append( random.choice(limage) )

    i = 0
    for X in range( grid_len ):
        for Y in range( grid_len ):
            choice = limage[ res[i] ]

            im = Image.open(choice )
            reuslt.paste(im, (X*img_resolution[0], Y*img_resolution[1]) )
            i+=1

    reuslt.save(ouputimg)

def makegrid_fixed_outputres(thumb_res, output_res, output_path, list_images, perline_target, padding):
    out_w,out_h = output_res[0],output_res[1]
    thumb_w,thumb_h = thumb_res[0],thumb_res[1]

    result = Image.new('RGB', (out_w,out_h))

    target_thumb_w = int( out_w/perline_target )
    p = target_thumb_w/thumb_w
    target_thumb_h = int( thumb_h*p)

    nrow = math.ceil( out_w/target_thumb_w )
    nline = math.ceil( out_h/target_thumb_h )

    print("-- Grid: {}/{}".format(nrow,nline))
    print("-- New resolution: {}/{}".format(target_thumb_w, target_thumb_h))

    amountofimages = nrow*nline
    if len(list_images) >= amountofimages:
        print("-- No duplicata")
        res = random.sample( range(0, len(list_images)), amountofimages)
    else:
        print("-- Duplicata")
        res = []
        li = list(range(0,len(list_images)))
        for i in range( amountofimages ):
            res.append( random.choice(li) )


    i=0
    for X in range( nrow ):
        for Y in range( nline ):
            choice = list_images[ res[i] ]

            im = Image.open(choice )
            im1 = im.resize( (target_thumb_w-padding, target_thumb_h-padding) )
            #print( X*target_thumb_w, Y*target_thumb_h )

            result.paste(im1, ( X*target_thumb_w, Y*target_thumb_h ) )
            i+=1


    
    result.save(output_path)

def decypher_system_name(system_name):
    nospace = system_name.strip()
    spl = nospace.split("-")

def cleanup_unidentified(imgfolder):
    limage = os.listdir(imgfolder)

    for image in limage:
        image_path = os.path.join( imgfolder,image )
        try:
            im = Image.open(image_path )
        except:
            os.rename(image_path, image_path+".NO")
    
def main_grid_creator(boxart_fold, system_name , output_resolution, ntiles, padding, ouputimg, only_compat_aspectratio = False, cleanup = False):
    print(system_name)
    if only_compat_aspectratio:
        resolution, limages  = get_resolution_onlyrescompatible(boxart_fold)
    else:
        resolution, limages  = get_resolution_allimages(boxart_fold)
    
    if resolution:
        if cleanup:
            cleanup_unidentified(boxart_fold)

        #ouputimg = os.path.join( thumb_fold, "{}.jpg".format( system_name ))
        makegrid_fixed_outputres(resolution, output_resolution, ouputimg, limages, ntiles, padding)

'''
###################################################
# This will run on libretro-thumbnails depots only
###################################################

thumb_fold = r"F:\libretro-thumbnails"
output_path = r"F:\RetroBat\emulationstation\.emulationstation\themes\MeringuePersonnal_ES_DE_Knulli\Tools\Make_Grid_generated"
i = 0
for system_name in os.listdir(thumb_fold):
    if not "git" in system_name:
        systemfold = os.path.join(thumb_fold, system_name )
        if os.path.isdir(systemfold) :
            for subfold in os.listdir(systemfold):
                if "Named_Boxarts" in subfold:
                    boxart_fold = os.path.join( systemfold, subfold)
                    ouputimg = os.path.join( output_path, (1920,1080), "{}.jpg".format( system_name ))

                    main_grid_creator(boxart_fold, system_name, 8, 10, ouputimg)
                    

            i+=1
            if i >= 300:
                break
                #break

'''

system_name = "gba"
boxart_fold = r"Y:\RG35XX\SD_card02\roms\gba\images"

output_path = r"F:\RetroBat\emulationstation\.emulationstation\themes\MeringuePersonnal_ES_DE_Knulli\_inc\systems\background_4_3"

ouputimg = os.path.join( output_path, "{}.jpg".format( system_name ))

main_grid_creator(boxart_fold, system_name, (960,720), 10, 5, ouputimg, only_compat_aspectratio= True)