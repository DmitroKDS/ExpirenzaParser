from device import start
from navigator import tap
import parse
from notify import notify

import time

driver = start()

time.sleep(5)

tap(driver, text="Див. усі")
time.sleep(1)

#Get starting data
boxes = {}

while True:
    xml = driver.page_source
    parsed_boxes = parse.boxes_ios(xml)

    if len(parsed_boxes)!=0 and parsed_boxes[0]['status'] != "Розпродано":
        while True:
            xml = driver.page_source
            parsed_boxes = parse.boxes_ios(xml)
            
            count = len(boxes)

            for box in parsed_boxes:
                if box['name'] is None:
                    continue 

                box_key = f"{box['name']} {box['sale_price']} / {box['real_price']}"
                if box['status'] != "Розпродано" and box_key not in boxes:
                    boxes[box_key] = box['status']
                    if "Milk" in box['name'] or "Namel" in box['name']:
                        notify(driver, f"🆕 Новий бокс: {box_key} - {box['status']}")
                        print(f"{box_key} - {box['status']}")

            if len(boxes)==count or len(parsed_boxes)!=0 and parsed_boxes[-1]['status'] == "Розпродано":
                driver.swipe(start_x=200, start_y=200, end_x=200, end_y=1400, duration=100)
                break


            driver.swipe(start_x=500, end_x=500, start_y=1000, end_y=200, duration=600)
            time.sleep(1)

    tap(driver, resource_id="back_button")
    time.sleep(1)
    tap(driver, text="Див. усі")
    time.sleep(2)


driver.quit()

# Вивід

# 
# 1.
# appium --log-level info


# 2.
# cd ~/.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent
# 
# xcodebuild -project WebDriverAgent.xcodeproj \
#   -scheme WebDriverAgentRunner \
#   -destination 'id=00008101-000214911A69001E' \
#   -allowProvisioningUpdates \
#   test

# xcodebuild -project WebDriverAgent.xcodeproj \
#   -scheme WebDriverAgentRunner \
#   -destination 'id=00008110-000241842651801E' \
#   -allowProvisioningUpdates \
#   test