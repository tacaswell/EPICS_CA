def test_connect():
    """Check that casput and caget work together"""
    PV_name = "TEST:TEST.VAL" 
    from ..CAServer import casput
    casput(PV_name,1)
    from ..CA import caget
    assert caget(PV_name) == 1

def _test_disconnect():
    """Check that 'casdel' disconnects a PV"""
    from ..CAServer import casput,casget,casdel
    from ..CA import caget
    from time import sleep

    PV_name = "TEST:TEST.VAL" 
    casput(PV_name,1)
    assert casget(PV_name) == 1
    assert caget(PV_name) == 1
    casdel(PV_name)
    sleep(5)
    assert casget(PV_name) is None
    sleep(0.1)
    assert caget(PV_name) is None
