<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<math xmlns="http://www.w3.org/1998/Math/MathML">
			<xsl:apply-templates/>
		</math>
	</xsl:template>
	
	<!-- Subscripts -->
	<!-- <xsl:template match="sub[preceding::node()[1] and following::line[1]]">
		<msub>
			<mrow><xsl:value-of select="current()[preceding::node()[1]]"/></mrow>
			<mrow><xsl:apply-templates select="current()[following::line[1]]"/></mrow>
		</msub>
	</xsl:template> -->
	
	<!-- General patterns -->
	<xsl:template match="line">
		<mrow>
			<xsl:apply-templates/>
		</mrow>
	</xsl:template>
	
	<xsl:template match="mi">
		<mi><xsl:value-of select="current()"/></mi>
	</xsl:template>
	
	<xsl:template match="mo">
		<mi><xsl:value-of select="current()"/></mi>
	</xsl:template>
	
</xsl:stylesheet>