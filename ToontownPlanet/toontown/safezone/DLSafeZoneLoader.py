from toontown.safezone import DLPlayground
from toontown.safezone import SafeZoneLoader
from toontown.toon import NPCToons


class DLSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DLPlayground.DLPlayground
        self.musicFile = 'phase_8/audio/bgm/DL_nbrhood.ogg'
        self.activityMusicFile = 'phase_8/audio/bgm/DL_SZ_activity.ogg'
        self.dnaFile = 'phase_8/dna/donalds_dreamland_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_DL_sz.pdna'
        #self.name = NPCToons.createLocalNPC(2020)
        #self.name.reparentTo(render)
        #self.name.setPos(30, 0, -15)
        #self.name.setH(88)
        #self.name = NPCToons.createLocalNPC(2018)
        #self.name.reparentTo(render)
        #self.name.setPos(30.8453, -3.07898, -14.975)
        #self.name.setH(88)
        #self.silly = loader.loadModel('phase_4/models/props/tt_a_ara_ttc_sillyMeter_default.bam')
        #self.silly.reparentTo(render)
        #self.silly.setPos (11.8052, 1.75063, -14.975)
        #self.name = NPCToons.createLocalNPC(2019)
        #self.name.reparentTo(render)
        #self.name.setPos(31.0835, -5.67733, -14.975)
        #self.name.setH(88)
        

                                    
   
