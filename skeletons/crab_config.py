from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

###REQUESTNAME
###config.General.requestName = 'WRtoNLtoLLJJ_WR1000_N100_MG_CMSSW_9_4_6_patch1_MINIAODSIM'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
###PSETNAME
###config.JobType.psetName = 'AODSIM__TO__MINIAODSIM__WRtoNLtoLLJJ_WR1000_N100_MG.py'
config.JobType.maxMemoryMB = 4000

###INPUTDATASET
###config.Data.inputDataset = '/WRtoNLtoLLJJ_WR1000_N100_MG/shjeon-CMSSW_8_0_21_AODSIM-e82b9d23b21065f4c0a0b29f84898dde/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'CMSSW_9_4_6_patch1_MINIAODSIM'
config.Data.ignoreLocality = True

config.Site.storageSite = 'T2_KR_KNU'
config.Site.whitelist = ['T2_*', 'T3_*']
config.Site.blacklist = ['T2_US_Wisconsin','T2_CH_CERN']

