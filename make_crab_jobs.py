import os

CHANNEL = "EE"


filelist_lines = file("skeletons/filelist_Zprime.txt").readlines()
crab_config_lines = file("skeletons/crab_config.py").readlines()


for i_filelist_lines in filelist_lines:
  if "ZprimetoNN_"+CHANNEL in i_filelist_lines:
    this_filename = i_filelist_lines.strip().split("/")[1]
    this_fileurl =  i_filelist_lines.strip()
#    print this_filename
#    print this_fileurl

    os.system("mkdir -p crab_"+this_filename)
    os.system("cp skeletons/AODSIM__TO__MINIAODSIM.py crab_"+this_filename+"/AODSIM__TO__MINIAODSIM__"+this_filename+".py")
    new_crab_config = file("crab_"+this_filename+"/crab_"+this_filename+".py", "wt")
    for i_crab_config_lines in crab_config_lines:
      this_line = i_crab_config_lines.strip()
      if "###REQUESTNAME" in this_line:
        new_crab_config.write("config.General.requestName = '"+this_filename+"_CMSSW_9_4_6_patch1_MINIAODSIM'\n")
      elif "PSETNAME" in this_line:
        new_crab_config.write("config.JobType.psetName = 'AODSIM__TO__MINIAODSIM__"+this_filename+".py'\n")
      elif "INPUTDATASET" in this_line:
        new_crab_config.write("config.Data.inputDataset = '"+this_fileurl+"'\n")
      else : new_crab_config.write(this_line+"\n")

    print "cd crab_"+this_filename
    print "crab submit -c crab_"+this_filename+".py"
    print "cd -"
