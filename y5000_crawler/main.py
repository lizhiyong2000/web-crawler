# from scrapy import cmdline
#
# import html2markdown
#
# import html2text


# content = '''
#
# <div class="lct_cont">
#                             <p>
# 	夏朝是中国古代由原始社会进入奴隶阶级社会的第一个王朝，为上古三代之首。关于夏朝的开始以及启又是如何继位的问题，历代以来，历史学家都没有统一说法。</p>
# <p>
# 	根据文献记载和古代传说，当时的中国原始氏族社会正在逐渐解体，聚居在黄河中 下游两岸的夏部族，通过与周围地区的其他部族联盟的形式，首先建立了中国历史上第一个奴隶制王朝，其统治时间大约从公元前 23世纪（另一说法为公元前21世纪）开始至前17世纪，近500年左右，直至其被商 汤所灭，共传14世，17王。</p>
# <p style="text-align: center;">
# 	<img src="https://img.y5000.com/uploads/allimg/170930/8-1F93010193aE.jpg" style="max-width:100%"></p>
# <p>
# 	在夏王朝建立之初，曾出现过夏部族 与周围其他部族之间争夺联盟首领的频繁 战争。由于禹治水有功和大力发展了农业生产，使得夏部族势力强大， 也博得了各部族首领的支持，从而顺利得到部族联盟首领的地位。</p>
# <p>
# 	其后，禹对三苗的战争又 取得胜利，进一步巩固了王权。夷、夏诸族首领完全臣服 于夏王朝的统治，成为维护王 权的世袭贵族。所谓“禹合诸 侯于涂山，执玉帛者万国”，正是后人追述夏王朝建立统治 地位时的情景。</p>
# <p>
# 	夏禹死后，其子启继承王位，这种废除了 “禅让"制度 而实行父传子的王位继承方式，立即引起争夺王位的激烈斗争。东方偃姓集团首领伯益，率先起兵反对夏启占据王位，结果伯益被启诛杀。西方的同姓邦国有扈氏也曾起兵， 但启亲率大军进行讨伐，有扈氏战败而被剿绝。</p>
# <p>
# 	夏启在巩固王位的激烈斗争中大获全胜后，众多邦国首领被他邀请到阳翟朝会，启在钧台举行宴会，这就是历史传说中有名的 “钧台之享”。至此，夏启最终确立了王位继承的“世袭”制。</p>
# <p>
# 	启巩固了王权统治后，对本部族和邦国进行了残酷的阶级压迫与剥削，但他自己却过着奢侈腐化的生活。此一依据来自《墨 子》，书中称启“好酒耽乐”，《楚辞•离骚》也说启“娱以自纵”。 不过无论事实如何，中国历史的发展的确是从那时开始，从“大同之世、天下为公”的原始社会，跳跃到了以“天下为家”的阶级社会。</p>
# <hr>
# <p>
# 	<span style="color:#ff0000;"><strong>下一节：</strong></span><strong><a href="https://www.y5000.com/sjls/25849.html"><span style="color:#ff0000;">汉莫拉比统一美索不达米亚平原</span></a></strong></p>
#
#                         </div>
# '''
#
#
# print(html2text.html2text(content))

# cmdline.execute("scrapy crawl y5000".split())
import os
import re


def validateTitle(title):

    if title.startswith('_'):
        title = title[1:]

    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]\.")
    title = rule.sub('_',title)
    #
    # rstr1 = r"…！？"
    #
    # title = re.sub(rstr1, "", title)
    #
    #
    # rstr = r"[\/\\\:\*\?\"\<\>\|《》，“”：、—]"  # '/ \ : * ? " < > |'
    # title = re.sub(rstr, "_", title)  # 替换为下划线

    title = re.sub(r"__", "_", title)
    title = re.sub(r"__md", ".md", title)
    title = re.sub(r"_md", ".md", title)
    title = re.sub(r"_.md", ".md", title)

    title = re.sub(r"__", "_", title)

    print(title)
    return title



cwd = os.getcwd()

path = os.path.join(cwd, "results")

dirList = os.listdir(path)
# print(fileList)

for dir in dirList:


    dir_path = os.path.join(path, dir)
    filesList = os.listdir(dir_path)

    for file_name in filesList:

        os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, validateTitle(file_name)))
        pass


