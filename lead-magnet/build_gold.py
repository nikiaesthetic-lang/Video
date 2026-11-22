"""Run lead-magnet build_pdf.py with a bright metallic-gold theme override."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("bp", "/root/.claude/skills/lead-magnet/scripts/build_pdf.py")
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
INK = "#3B2A08"
GOLD = """
.cover{background:linear-gradient(135deg,#FFF6D2 0%%,#F3D774 28%%,#D9B440 52%%,#F7E39A 74%%,#CFA531 100%%);color:#3B2A08}
.cover:before{background:radial-gradient(circle at 35%% 35%%,#FFFDF0 0%%,#F6DE8A 50%%,#D7B03E 100%%);opacity:.75}
.cover .tag{background:#3B2A08;color:#F7E39A}
.cover .sub{opacity:1}
.cover .by{border-top:1px solid rgba(59,42,8,.35)}
h1{border-bottom-color:#D9B440}
h2{color:#9C7614}
th{background:linear-gradient(90deg,#F3D774,#D9B440);color:#3B2A08}
.tip{background:#FFF8E0;border-left-color:#D9B440}
ul.check i{border-color:#D9B440}
ol.steps li:before{background:linear-gradient(135deg,#F7E39A,#D9B440);color:#3B2A08}
.next{background:#FFF8E0}
.next .btn{background:linear-gradient(135deg,#F7E39A 0%%,#D9B440 55%%,#C29A2E 100%%);color:#3B2A08}
"""
bp.CSS = bp.CSS + GOLD
bp.main()
