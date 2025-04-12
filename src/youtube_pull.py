from webscraper.base import RPA_BASE
from time import sleep
import time
import json
class YoutubePull(RPA_BASE):
    
    def __init__(self, playlist_url:str, playlist_name:str)->None:
        self.playlist_url = playlist_url
        self.playlist_name = playlist_name
        self.driver = self.return_driver()
        self.script = """
        let goToBottom = setInterval(() => window.scrollBy(0, 400), 1000);
                                   
        clearInterval(goToBottom);
        let arrayVideos = [];
        console.log(" ".repeat(50));
        const links = document.querySelectorAll('a');
        for (const link of links) {
        if (link.id === 'video-title') {
            link.href = link.href.split('&list=')[0];
            arrayVideos.push(link.title + ';' + link.href);
            console.log(link.title + '\t' + link.href);
        }
        }
        let data = arrayVideos.join(' ');
        let blob = new Blob([data], {type: 'text/csv'});
        let elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = 'my_data.csv';
        document.body.appendChild(elem);
        elem.click();
        document.body.removeChild(elem);
    """
        print(self.script)
     
    def _go_to_playlist(self):
        self.driver.get(self.playlist_url)
        self.wait_and_click(driver=self.driver, element_id='//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button', element_type='xpath')
    def _scroll_playlist(self):
        self.driver.execute_script('let goToBottom = setInterval(() => window.scrollBy(0, 400), 1000);')
    def _get_playlist_metadata(self):
        current_time = time.localtime()
        formatted_time = time.strftime("%d%m%y%H%M", current_time)
        save_path = r'E:/Repositories/CloudFlow/data'
        file_name = rf'{self.playlist_name}_data_{formatted_time}'
        save = json.dumps(rf'{save_path}/{file_name}')
        self.driver.execute_script("""
        let arrayVideos = [];
        console.log(" ".repeat(50));
        const links = document.querySelectorAll('a');
        for (const link of links) {
        if (link.id === 'video-title') {
            link.href = link.href.split('&list=')[0];
            arrayVideos.push(link.title + ';' + link.href);
            console.log(link.title + '\t' + link.href);
        }
        }
        let data = arrayVideos.join(' ');
        let blob = new Blob([data], {type: 'text/csv'});
        let elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = arguments[0];
        document.body.appendChild(elem);
        elem.click();
        document.body.removeChild(elem);
                                   """, save )
    def _save_metadata(self):
        self.driver.execute_script("""
        let data = arrayVideos.join(' ');
        let blob = new Blob([data], {type: 'text/csv'});
        let elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = arguments[0];
        document.body.appendChild(elem);
        elem.click();
        document.body.removeChild(elem);""", )
    
    def _ex_all(self):
        self.driver.execute_script(self.script)
    
    def run(self):
        self._go_to_playlist()
        sleep(2)
        self._scroll_playlist()
        sleep(25)
        self._get_playlist_metadata()
        sleep(10)
        return True

if __name__=='__main__':
    ytp=YoutubePull('https://www.youtube.com/playlist?list=PLLr1_JG3LWAq2xbRWvkPFE9oqYgKKLi7u', 'HolyQuraan')
    ytp.run()

