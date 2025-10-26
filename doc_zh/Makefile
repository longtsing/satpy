# Sphinx 文档的 Makefile
#

# 您可以从命令行设置这些变量。
SPHINXOPTS    = -n
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build

# 内部变量。
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html dirhtml pickle json htmlhelp qthelp latex changes linkcheck doctest

help:
	@echo "请使用 \`make <target>' 其中 <target> 是以下之一"
	@echo "  html      生成独立的HTML文件"
	@echo "  dirhtml   在目录中生成名为index.html的HTML文件"
	@echo "  pickle    生成pickle文件"
	@echo "  json      生成JSON文件"
	@echo "  htmlhelp  生成HTML文件和HTML帮助项目"
	@echo "  qthelp    生成HTML文件和qthelp项目"
	@echo "  latex     生成LaTeX文件，您可以设置PAPER=a4或PAPER=letter"
	@echo "  changes   生成所有已更改/已添加/已弃用项目的概览"
	@echo "  linkcheck 检查所有外部链接的完整性"
	@echo "  doctest   运行文档中嵌入的所有doctest（如果启用）"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "构建完成。HTML页面位于 $(BUILDDIR)/html。"

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "构建完成。HTML页面位于 $(BUILDDIR)/dirhtml。"

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "构建完成；现在您可以处理pickle文件。"

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "构建完成；现在您可以处理JSON文件。"

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "构建完成；现在您可以在 $(BUILDDIR)/htmlhelp 中使用HTML Help Workshop运行" \
	      ".hhp项目文件。"

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "构建完成；现在您可以在 $(BUILDDIR)/qthelp 中使用 "qcollectiongenerator" 运行" \
	      ".qhcp项目文件，像这样："
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/NWCSAFMSGPP.qhcp"
	@echo "要查看帮助文件："
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/NWCSAFMSGPP.qhc"

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "构建完成；LaTeX文件位于 $(BUILDDIR)/latex。"
	@echo "在该目录中运行 \`make all-pdf' 或 \`make all-ps'" \
	      "以通过(pdf)latex运行这些文件。"

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "概览文件位于 $(BUILDDIR)/changes。"

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "链接检查完成；在上面的输出或 $(BUILDDIR)/linkcheck/output.txt 中查找任何错误。"

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "源代码中的doctest测试完成，查看 $(BUILDDIR)/doctest/output.txt 中的结果。"
