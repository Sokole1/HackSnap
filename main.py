from geturl import get_link

url_history = {}
items = []

def add_to_urls(group, subject, level, year, month):
    items.clear()
    items.append(subject)
    items.append(level)
    items.append(year)
    items.append(month)
    url = get_link(group, subject, level, year, month)
    url_history[" ".join(items)] = url

add_to_urls("5", "Mathematics", "HL", "2005", "May")
add_to_urls("5", "Mathematics", "SL", "2005", "May")
add_to_urls("4", "Biology", "HL", "2010", "November")
add_to_urls("1", "English", "HL", "2016", "May")
add_to_urls("5", "Mathematics", "HL", "2005", "May")
add_to_urls("5", "Mathematics", "HL", "2005", "May")

#{'5 Mathematics HL 2005 May': 'https://examsnap.io/files/index.php/s/IB_Past_Papers?path=%2FGroup%205%20-%20Mathematics%2FMathematics%20HL%2F2005%20May%20Examination%20Session'}