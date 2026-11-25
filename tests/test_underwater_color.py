import pytest
import imaging.underwater_color as mod

CASES = [
    ("depth_attenuation", (1,)),
    ("scatter_mask", (1,)),
    ("fill_light_wb", (1,)),
    ("temporal_stabilize", (1,)),
    ("mosaic_joint_wb", (1,)),
    ("red_channel_limit", (1,)),
    ("load_underwater", (1,)),
    ("estimate_backscatter", (1,)),
    ("restore_color", (1,)),
    ("present_uw", (1,)),
    ("validate_uw", (1,)),
    ("metrics_uw", (1,)),
    ("audit_uw", (1,)),
    ("fallback_uw", (1,)),
    ("determinism_uw", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
