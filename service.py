import core
import classify_image
import time
import json

run = True
while(run):

    while (run):
        message = core.checkTasks()
        if "task" in message:
            #core.downloadImage(message["task"])
            string, score = classify_image.run_inference_on_image("images/"+str(message["task"])+".jpg")
            result = {
                "task":message["task"],
                "result":string,
                "score":float(score)
            }
            print(result)

            core.sendMessageToFrontend(json.dumps(result))
        else:
            time.sleep(10)
