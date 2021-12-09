from ampel import FsmEfe
import time


class AmpelFsm(FsmEfe):
    pass


#ampel = FsmEfe("ROT", "GELB", "GRÜN", 10, 2, 10)
ampel2 = FsmEfe()



while True:

    ampel2.kirmiziyi_yak()

    ampel2.sariyi_yak()

    ampel2.yesili_yak()


