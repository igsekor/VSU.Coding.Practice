head = "\t<head>\n\t\t<meta charset=\"UTF-8\">\n\t\t<title>First page</title>\n\t</head>\n"
body_begin = "\t<body>\n"
body_end = "\t</body>\n"

html = "<!DOCTYPE html>\n<html lang=\"en\">\n" + head + body_begin
html += "\t\t<h1>Factorial</h1>\n\t\t<ul>\n"

f = 1
for i in range(1, 10):
    f = f * i
    html += "\t\t\t<li>{0}</li>".format(f) + "\n"

html += "\t\t</ul>\n" + body_end + "</html>"

index_file = open("index.html", "w")
index_file.write(html)
index_file.close()