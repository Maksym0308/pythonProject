import lxml.etree

html = """<html>
<div data-testid="jobSearch-Yosegi" class="css-1r8ocvi eu4oa1w0">
    <div class="jobsearch-MosaicProviderRichSearch css-1lqrrhf eu4oa1w0">
        <div id="MosaicProviderRichSearchDaemon" class="mosaic MosaicProviderRichSearchDaemon mosaic-provider-hydrated">
            <div role="search" class="dd-privacy-allow">
                <div class="yosegi-InlineWhatWhere css-u74ql7 eu4oa1w0">
                    <form class="yosegi-InlineWhatWhere-form yosegi-InlineWhatWhere--desktopTstHpForm" id="jobsearch" method="get" action="/jobs?q=&amp;l=&amp;from=searchOnHP">
                        <div class="css-b7sqy0 eu4oa1w0">
                            <div class="css-1uoj1e2 eu4oa1w0">
                                <div class="css-1mjgtgv eu4oa1w0">
                                    <span class="css-8u2krs esbq1260">Keyword : all jobs</span>
                                    <div class="css-46bpn7 e37uo190">
                                        <div class="css-127l7d5 e1ttgm5y0">
                                            <span class="css-2ovn2v e6fjgti1">
                                                <span class="css-khw5xy e6fjgti0">
                                                    <svg xmlns="http://www.w3.org/2000/svg" focusable="false" role="img" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true" class="css-8548fo eac13zx0">
                                                        <path fill-rule="evenodd" d="M14.4959 15.9106c-1.2016.9066-2.6973 1.4441-4.3185 1.4441C6.2134 17.3547 3 14.1413 3 10.1774 3 6.2134 6.2134 3 10.1774 3c3.9639 0 7.1773 3.2134 7.1773 7.1774 0 1.6215-.5377 3.1174-1.4445 4.3191l4.7969 4.7969c.3906.3905.3906 1.0237 0 1.4142-.3905.3906-1.0236.3906-1.4142 0l-4.797-4.797zm.8588-5.7332c0 2.8593-2.318 5.1773-5.1773 5.1773C7.318 15.3547 5 13.0367 5 10.1774 5 7.318 7.318 5 10.1774 5c2.8593 0 5.1773 2.318 5.1773 5.1774z" clip-rule="evenodd"></path>
                                                    </svg>
                                                </span>
                                                <input aria-invalid="false" id="text-input-what" name="q" type="text" placeholder="Cargo, palavras-chave ou empresa" aria-label="search: Job title, keywords, or company" class="css-4pnak9 e1jgz0i3">
                                                <span class="css-r13ok1 e6fjgti0"></span>
                                            </span>
                                            <div id="ifl-FormField-errorText-1" class="css-u74ql7 eu4oa1w0"></div>
                                        </div>
                                    </div>
                                </div>
                                <div role="separator" aria-orientation="vertical" class="css-ofyd6b e15p7aqh1"></div>
                                <div class="css-164w3g1 eu4oa1w0">
                                    <span class="css-8u2krs esbq1260">Edit location input box label</span>
                                    <div class="css-46bpn7 e37uo190">
                                        <div class="css-16d6dy1 e1ttgm5y0">
                                            <span class="css-kyeb8v e6fjgti1">
                                                <span class="css-khw5xy e6fjgti0">
                                                    <svg xmlns="http://www.w3.org/2000/svg" focusable="false" role="img" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true" class="css-8548fo eac13zx0">
                                                        <path d="M12 2C8.13 2 5 5.13 5 9c0 4.5229 5.1954 11.0927 6.6344 12.8256.1934.2329.5378.2329.7312 0C13.8046 20.0927 19 13.5229 19 9c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"></path>
                                                    </svg>
                                                </span>
                                                <input aria-invalid="false" id="text-input-where" name="l" type="text" placeholder="Cidade, estado, região ou “remoto”" aria-label="Editar local" class="css-4pnak9 e1jgz0i3">
                                                <span class="css-r13ok1 e6fjgti0"></span>
                                            </span>
                                            <div id="ifl-FormField-errorText-6" class="css-u74ql7 eu4oa1w0"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="css-uzyy91 eu4oa1w0">
                                <button class="yosegi-InlineWhatWhere-primaryButton" type="submit">Achar vagas</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</html>
"""

def parse_html():
    tree = lxml.etree.HTML(html)

    input_search = tree.xpath('//*[@id="text-input-what"]')
    print(input_search[0].attrib['placeholder'])

    input_location = tree.xpath('//*[@id="text-input-where"]')
    print(input_location[0].attrib['placeholder'])

    button_jobsearch = tree.xpath('//*[@id="jobsearch"]/div/div[2]/button')
    print(button_jobsearch[0].text)

if __name__ == "__main__":
    parse_html()