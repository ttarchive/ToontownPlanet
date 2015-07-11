from toontown.safezone import SafeZoneLoader
from toontown.safezone import TTPlayground
from toontown.toon import NPCToons

class TTSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = TTPlayground.TTPlayground
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg'
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.dnaFile = 'phase_4/dna/toontown_central_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_4/dna/storage_TT_sz.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird2.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird3.ogg'])
        bank = self.geom.find('**/*toon_landmark_TT_bank_DNARoot')
        onScreenDebug.add('Avatar Position', localAvatar.getPos())
        onScreenDebug.add('Avatar Angle', localAvatar.getHpr())
        x = localAvatar.getPos().get_x()
        y = localAvatar.getPos().get_y()
        doorTrigger = bank.find('**/door_trigger*')
        doorTrigger.setY(doorTrigger.getY() - 1.5)
        #self.piano = loader.loadModel('phase_6/models/props/piano.bam')
        #self.piano.reparentTo(render)
        #self.piano.setPosHpr (85.91, 149.76, 2.61, 327.99, 0, 0)
        #self.safe = loader.loadModel('phase_5.5/models/char/Clarabelle-zero.bam')
        #self.safe.reparentTo(render)
        #self.safe.setPos (100.003, 10.192, 4.025)
        #self.name = NPCToons.createLocalNPC(2005)
        #self.name.reparentTo(render)
        #self.name.setPos(30, -8, 4)
        #self.name.setH(88)
        #self.name = NPCToons.createLocalNPC(2024)
        #self.name.reparentTo(render)
        #self.name.setPos(102, -8, 4)
        #self.name.setH(88)
        #self.shop = loader.loadModel ('phase_5/models/modules/TT_C1_raised.bam')
        #self.shop.reparentTo(render)
        #self.shop.setPos (49.7016, 22.4342, 4.02495)
        #self.fountain = loader.loadModel ('phase_4/models/props/toontown_central_fountain.bam')
        #self.fountain.reparentTo(render)
        #self.fountain.setPos (77.3244, -112.119, 2.525)
        #self.door = loader.loadModel ('phase_6/models/modules/DD_doors.bam')
        #self.door.reparentTo(render)
        #self.door.setPos (59.139, 18.3468, 4.025)
        #if x =51.2807 and x = -51.2807 and y = 68.5157 and y = -68.5157 and loadedArea = 'toontowncenteral'
        #toontowncentral = loader.unloadModel('phase_4/models/neighborhoods/toontown_central_full.bam')
        #shop = loader.loadModel ('phase_4/models/modules/ttc_library_interior.bam')
        #loadedArea = 'shop'
        #shop.reparentTo(render)
        #localAvatar.setPos(-310.387)

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)

          
        del self.birdSound
        #del self.name
        #del self.shop
        #del self.fountain
        #del self.piano

