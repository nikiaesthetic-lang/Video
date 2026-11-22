"""Run lead-magnet build_pdf.py with a light powder-blue theme override."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("bp", "/root/.claude/skills/lead-magnet/scripts/build_pdf.py")
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
INK = "#3B2A08"
GOLD = """
.cover{background:linear-gradient(135deg,#F7FBFF 0%%,#DDECF8 28%%,#C4DDF1 52%%,#E8F2FB 74%%,#B9D6EE 100%%);color:#1F3550}
.cover:before{background:radial-gradient(circle at 35%% 35%%,#FFFFFF 0%%,#E3EFF9 48%%,#BDD8EE 100%%);opacity:.85}
.cover .tag{background:#1F3550;color:#E3EFF9}
.cover .sub{opacity:1}
.cover .by{border-top:1px solid rgba(31,53,80,.25)}
h1{border-bottom-color:#A9CBE6}
h2{color:#3A6A96}
th{background:linear-gradient(90deg,#DDECF8,#B9D6EE);color:#1F3550}
tbody tr:nth-child(even) td{background:#F3F8FC}
.tip{background:#F1F7FC;border-left-color:#A9CBE6}
ul.check i{border-color:#8DB8DC}
ol.steps li:before{background:linear-gradient(135deg,#E3EFF9,#B9D6EE);color:#1F3550}
.next{background:#F1F7FC}
.next .btn{background:linear-gradient(135deg,#E3EFF9 0%%,#B9D6EE 55%%,#9CC3E3 100%%);color:#1F3550}
"""
bp.CSS = bp.CSS + GOLD
bp.main()
