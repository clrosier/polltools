from polltools import SitePoller

if __name__ == "__main__":
    s = SitePoller("http://www.algonquinpark.on.ca/news/2020/2020-03-14_covid19.php", poll_interval=3)
    s.poll()