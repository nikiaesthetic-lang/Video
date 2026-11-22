"""Run lead-magnet build_pdf.py with a bright rose-gold theme override."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("bp", "/root/.claude/skills/lead-magnet/scripts/build_pdf.py")
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
INK = "#3B2A08"
GOLD = """
.cover{background:linear-gradient(135deg,#FFF4EE 0%%,#FBDCCD 26%%,#F1BCA6 50%%,#FCE3D6 72%%,#EBB29A 100%%);color:#5A2A1E}
.cover:before{background:radial-gradient(circle at 35%% 35%%,#FFFFFF 0%%,#FBE0D3 48%%,#EDB49C 100%%);opacity:.8}
.cover .tag{background:#5A2A1E;color:#FCE3D6}
.cover .sub{opacity:1}
.cover .by{border-top:1px solid rgba(90,42,30,.3)}
h1{border-bottom-color:#E9AE96}
h2{color:#B5634B}
th{background:linear-gradient(90deg,#FBD9CA,#EDB49C);color:#5A2A1E}
.tip{background:#FFF3EE;border-left-color:#E9AE96}
ul.check i{border-color:#E9AE96}
ol.steps li:before{background:linear-gradient(135deg,#FCE3D6,#EDB49C);color:#5A2A1E}
.next{background:#FFF3EE}
.next .btn{background:linear-gradient(135deg,#FCE3D6 0%%,#EDB49C 55%%,#DE9C82 100%%);color:#5A2A1E}
"""
bp.CSS = bp.CSS + GOLD
bp.main()
