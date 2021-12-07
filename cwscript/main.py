from cwscript import CWScriptCompiler

compiler = CWScriptCompiler()
compiler.add_src_file("test_contract.cws")
compiler.compile("output_dir")
