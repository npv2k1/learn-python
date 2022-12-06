function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
let url=[]
async function a(){
   $x(
     '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/i'
   )[0].click();
    await sleep(1);
    url.push(this.document.URL);
    await a();
    console.log(url)
}