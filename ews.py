import pyautogui
import time
import os
import tkinter
import threading
import random
import datetime
import winsound
import sys


def Program():
    global stepCount, now, playAgain, needBreak, logMessage, fightChar, troopChar, battles_done, battles_done_text, play_again_color, play_again_x, play_again_y, start_color, start_x, start_y
    # pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True

    print('Press Ctrl-C to quit.')

    #play_again_x, play_again_y = pyautogui.position()
    #im = pyautogui.screenshot()
    #if play_again_x < 1920:
    #    play_again_color = im.getpixel((play_again_x, play_again_y))

    #start_x, start_y = pyautogui.position()
    #if start_x < 1920:
    #    start_color = im.getpixel((start_x, start_y))

    settingsFile = open('ews.txt').read()
    #print(settingsFile.readlines()[1])
    lines = settingsFile.split('.')
    play_again_x = int(lines[0])
    play_again_y = int(lines[1])
    old_pac = lines[2]
    pac = old_pac.split('(')
    pac = pac[1].split(')')
    pac = pac[0].split(',')
    play_again_color = (int(pac[0]), int(pac[1]), int(pac[2]))
    #play_again_color = lines[2]
    start_x = int(lines[3])
    start_y = int(lines[4])
    old_sc = lines[5]
    sc = old_sc.split('(')
    sc = sc[1].split(')')
    sc = sc[0].split(',')
    start_color = (int(sc[0]), int(sc[1]), int(sc[2]))
    close_x = play_again_x-154
    close_y = play_again_y
    play_x = play_again_x-118
    play_y = play_again_y-32
    missions_x = play_again_x-431
    mission1_y = play_again_y-208
    mission2_y = play_again_y-174
    mission3_y = play_again_y-130
    mission4_y = play_again_y-92
    mission5_y = play_again_y-67
    missionF_y = play_again_y-20
    prev_chapter_x = play_again_x-519
    prev_chapter_y = play_again_y-130
    next_chapter_x = play_again_x+219
    next_chapter_y = play_again_y-135
    #start_color = lines[5]
    print(play_again_color)


    def async_play_again():
        thread = threading.Thread(target=snap_play_again)
        #thread.daemon = True
        thread.start()

    def async_start():
        thread = threading.Thread(target=snap_start)
        #thread.daemon = True
        thread.start()

    def snap_play_again():
        global play_again_color, play_again_x, play_again_y, im
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking play again in 5\n")
        time.sleep(1)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking play again in 4\n")
        time.sleep(1)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking play again in 3\n")
        time.sleep(1)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking play again in 2\n")
        time.sleep(1)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking play again in 1\n")
        time.sleep(1)
        play_again_x2, play_again_y2 = pyautogui.position()
        im = pyautogui.screenshot()
        play_again_color2 = im.getpixel((play_again_x2, play_again_y2))
        s = open("ews.txt").read()
        s = s.replace(str(old_pac), str(play_again_color2))
        s = s.replace(str(play_again_x), str(play_again_x2))
        s = s.replace(str(play_again_y), str(play_again_y2))
        f = open("ews.txt", 'w')
        f.write(s)
        f.close()
        play_again_color = play_again_color2
        play_again_x = play_again_x2
        play_again_y = play_again_y2
        print(play_again_color)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Done\n")

    def snap_start():
        global start_color, start_x, start_y, im
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking start in 5\n")
        time.sleep(1)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking start in 4\n")
        time.sleep(1)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking start in 3\n")
        time.sleep(1)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking start in 2\n")
        time.sleep(1)
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Picking start in 1\n")
        time.sleep(1)
        start_x2, start_y2 = pyautogui.position()
        im = pyautogui.screenshot()
        start_color2 = im.getpixel((start_x2, start_y2))
        s = open("ews.txt").read()
        s = s.replace(str(old_sc), str(start_color2))
        s = s.replace(str(start_x), str(start_x2))
        s = s.replace(str(start_y), str(start_y2))
        f = open("ews.txt", 'w')
        f.write(s)
        f.close()
        start_x = start_x2
        start_y = start_y2
        start_color = start_color2
        text.insert('1.0', datetime.datetime.now().strftime("%H:%M:%S") + "Done\n")


    def color_loc():
        global im
        while True:
            im = pyautogui.screenshot()
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            if x < 1920:
                position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + ' Colors : ' + str(im.getpixel((x, y)))
                print(position_str, end='')
                print('\b' * len(position_str), end='', flush=True)


    needBreak = False
    logMessage = ""
    fightChar = '2,3'
    troopChar = 'q,w,e,r,t,y,u'
    battles_done = 0
    stepCount = 0
    playAgain = True


    def farm_quest():
        global stepCount, now, playAgain, needBreak, logMessage, fightChar, troopChar, battles_done, battles_done_text, play_again_color, play_again_x, play_again_y, start_color, start_x, start_y
        needBreak = False
        playAgain = True
        fight_start = datetime.datetime.now()
        battles_done = 0
        pyautogui.click(play_x, play_y)
        while True:
            now = datetime.datetime.now()
            if needBreak:
                text.insert('1.0', now.strftime("%H:%M:%S") + " stopping.\n")
                break
            try:
                to_battle = int(wasteEntry.get('1.0', tkinter.END))
            except:
                try:
                    to_battle = wasteEntry.get().split(',')
                except:
                    to_battle = "s"
            # print(to_battle)
            # print(battles_done)
            if not isinstance(to_battle,(list,)) and is_number(to_battle):
                # print("its a number")
                if battles_done == to_battle:
                    # print("playing sound")
                    text.insert('1.0', now.strftime("%H:%M:%S") + " Reached battles, stopping.\n")
                    duration = 500  # millisecond
                    freq = 500  # Hz
                    winsound.Beep(freq, duration)
                    duration = 500  # millisecond
                    freq = 37  # Hz
                    winsound.Beep(freq, duration)
                    duration = 500  # millisecond
                    freq = 500  # Hz
                    winsound.Beep(freq, duration)
                    break
            elif len(to_battle) > 1 and len(to_battle) > stepCount:
                commands = to_battle
                last_step = "s"
                for step in commands:
                    if needBreak:
                        text.insert('1.0', now.strftime("%H:%M:%S") + " stopping.\n")
                        stepCount = 0
                        break
                    print(step)
                    if is_number(last_step):
                        while not pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.press(troopChar[0])  # Press first troopChar first
                            pyautogui.press(troopChar[random.randint(0, troop_count)])
                            time.sleep(1)
                    if is_number(step):
                        time.sleep(1)
                        pyautogui.click(play_x, play_y)
                        to_battle = step
                        last_step = step
                        battles_done = 0
                        text.insert('1.0', now.strftime("%H:%M:%S") + " Doing " + to_battle + " battles\n")
                        while battles_done < int(to_battle):
                            if needBreak:
                                text.insert('1.0', now.strftime("%H:%M:%S") + " stopping.\n")
                                break
                            if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color) and playAgain:
                                fight_duration = datetime.datetime.now() - fight_start
                                fight_duration = divmod(fight_duration.days * 86400 + fight_duration.seconds, 60)
                                if fight_duration[1] > 0 or fight_duration[0] > 0:
                                    battles_done += 1
                                    text.insert('1.0', now.strftime("%H:%M:%S") + " Fight Duration: " + str(
                                        fight_duration[0]) + "m" + str(
                                        fight_duration[1]) + "s" + ". Troops: " + troopCharEntry.get() + "\n")
                                    battles_done_text.set("Battles done: " + str(battles_done))
                                logMessage = "Clicking Play Again."
                                text.insert('1.0', now.strftime("%H:%M:%S") + " Clicking Play Again.\n")
                                pyautogui.click(play_again_x, play_again_y)
                                time.sleep(1)
                            if pyautogui.pixelMatchesColor(start_x, start_y, start_color):
                                logMessage = "Clicking Start."
                                text.insert('1.0', now.strftime("%H:%M:%S") + " Clicking Start.\n")
                                pyautogui.click(start_x, start_y)
                                #time.sleep(1)
                            if logMessage != "Fighting.":
                                logMessage = "Fighting."
                                fight_start = datetime.datetime.now()
                                text.insert('1.0', now.strftime("%H:%M:%S") + " Fighting.\n")
                                #time.sleep(1)
                            log_count = int(text.index('end-1c').split('.')[0])
                            if log_count > 23:
                                text.delete("end-1c linestart", "end")
                            time.sleep(0.1)
                            troopChar = troopCharEntry.get().split(',')
                            troop_count = len(troopChar) - 1
                            if stepCount < 1:
                                pyautogui.press(troopChar[0])  # Press first troopChar first
                                pyautogui.press(troopChar[random.randint(0, troop_count)])
                                time.sleep(0.1)
                            else:
                                pyautogui.press(troopCharNew)  # Press first troopChar first
                                time.sleep(0.1)

                            fightChar = fightCharEntry.get().split(',')
                            fight_count = len(fightChar) - 1
                            pyautogui.press(fightChar[random.randint(0, fight_count)])
                        stepCount += 1
                    elif step == "next":
                        stepCount += 1
                        last_step = "s"
                        if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.click(close_x, close_y)
                            time.sleep(2)
                        pyautogui.click(next_chapter_x, next_chapter_y)
                        time.sleep(2)
                    elif step == "prev":
                        stepCount += 1
                        last_step = "s"
                        if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.click(close_x, close_y)
                            time.sleep(2)
                        pyautogui.click(prev_chapter_x, prev_chapter_y)
                        time.sleep(2)
                    elif step == "ch1":
                        stepCount += 1
                        last_step = "s"
                        if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.click(close_x, close_y)
                            time.sleep(2)
                        pyautogui.click(missions_x, mission1_y)
                        time.sleep(2)
                    elif step == "ch2":
                        stepCount += 1
                        last_step = "s"
                        if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.click(close_x, close_y)
                            time.sleep(2)
                        pyautogui.click(missions_x, mission2_y)
                        time.sleep(2)
                    elif step == "ch3":
                        stepCount += 1
                        last_step = "s"
                        if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.click(close_x, close_y)
                            time.sleep(2)
                        pyautogui.click(missions_x, mission3_y)
                        time.sleep(2)
                    elif step == "ch4":
                        stepCount += 1
                        last_step = "s"
                        if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.click(close_x, close_y)
                            time.sleep(2)
                        pyautogui.click(missions_x, mission4_y)
                        time.sleep(2)
                    elif step == "ch5":
                        stepCount += 1
                        last_step = "s"
                        if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.click(close_x, close_y)
                            time.sleep(2)
                        pyautogui.click(missions_x, mission5_y)
                        time.sleep(2)
                    elif step == "ch6":
                        stepCount += 1
                        last_step = "s"
                        if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color):
                            pyautogui.click(close_x, close_y)
                            time.sleep(2)
                        pyautogui.click(missions_x, missionF_y)
                        time.sleep(2)
                    else:
                        stepCount += 1
                        last_step = "s"
                        troopCharNew = step
            if pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color) and playAgain:
                fight_duration = datetime.datetime.now() - fight_start
                fight_duration = divmod(fight_duration.days * 86400 + fight_duration.seconds, 60)
                if fight_duration[1] > 0 or fight_duration[0] > 0:
                    battles_done += 1
                    text.insert('1.0', now.strftime("%H:%M:%S") + " Fight Duration: " + str(fight_duration[0]) + "m" + str(
                        fight_duration[1]) + "s" + ". Troops: " + troopCharEntry.get() + "\n")
                    battles_done_text.set("Battles done: " + str(battles_done))
                logMessage = "Clicking Play Again."
                text.insert('1.0', now.strftime("%H:%M:%S") + " Clicking Play Again.\n")
                pyautogui.click(play_again_x, play_again_y)
                time.sleep(0.1)
            if pyautogui.pixelMatchesColor(start_x, start_y, start_color):
                logMessage = "Clicking Start."
                text.insert('1.0', now.strftime("%H:%M:%S") + " Clicking Start.\n")
                pyautogui.click(start_x, start_y)
                #time.sleep(1)
            if logMessage != "Fighting.":
                logMessage = "Fighting."
                fight_start = datetime.datetime.now()
                text.insert('1.0', now.strftime("%H:%M:%S") + " Fighting.\n")
                #time.sleep(1)
            log_count = int(text.index('end-1c').split('.')[0])
            if log_count > 23:
                text.delete("end-1c linestart", "end")
            print(wasteEntry.get())
            if wasteEntry.get() == "d" and not pyautogui.pixelMatchesColor(play_again_x, play_again_y, play_again_color) and not pyautogui.pixelMatchesColor(start_x, start_y, start_color):
                fightChar = fightCharEntry.get()
                pyautogui.keyDown('d')
                time.sleep(4)
                pyautogui.keyUp('d')
                pyautogui.press(fightChar)
            time.sleep(0.1)
            troopChar = troopCharEntry.get().split(',')
            troop_count = len(troopChar) - 1
            if stepCount < 1:
                pyautogui.press(troopChar[0])  # Press first troopChar first
                pyautogui.press(troopChar[random.randint(0, troop_count)])
                time.sleep(0.1)
            else:
                pyautogui.press(troopCharNew)  # Press first troopChar first
                time.sleep(0.1)

            fightChar = fightCharEntry.get().split(',')
            fight_count = len(fightChar) - 1
            pyautogui.press(fightChar[random.randint(0, fight_count)])



    def farm_start():
        wasteEntry.focus()
        thread = threading.Thread(target=farm_quest)
        #thread.daemon = True
        thread.start()


    #thread2 = Thread(target=color_loc)
    #thread2.start()


    def stop_farm_quest():
        global needBreak, battles_done
        wasteEntry.focus()
        battles_done = 0
        needBreak = True


    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False


    try:
        #while True:
            #color_loc()
            #farm_quest()
        top = tkinter.Tk()
        # Buttons

        farmButton = tkinter.Button(top, text="Farm Quest", command=farm_start)
        farmButton.pack(side=tkinter.TOP)
        playAgainButton = tkinter.Button(top, text="Save Play Again", command=async_play_again)
        startButton = tkinter.Button(top, text="Save Start", command=async_start)
        playAgainButton.pack(side=tkinter.TOP)
        startButton.pack(side=tkinter.TOP)
        farmButtonStop = tkinter.Button(top, text="Stop Farm", command=stop_farm_quest)
        farmButtonStop.pack(side=tkinter.TOP)
        # Log
        text = tkinter.Text()
        text.insert(tkinter.END, "Loading...\n Find top of G in Again with Save Play Again\n")
        text.pack(side=tkinter.BOTTOM)
        # Inputs
        wasteEntry = tkinter.Entry(bd=2)
        wasteEntry.pack(side=tkinter.BOTTOM)

        fightCharLabel = tkinter.Label(top, text="Fight Key")
        fightCharLabel.pack(side=tkinter.LEFT)
        fightCharEntry = tkinter.Entry(top, bd=2)
        fightCharEntry.pack(side=tkinter.LEFT)
        fightCharEntry.insert(tkinter.END, fightChar)
        troopCharLabel = tkinter.Label(top, text="Troop Key")
        troopCharLabel.pack(side=tkinter.RIGHT)
        troopCharEntry = tkinter.Entry(top, bd=2)
        troopCharEntry.pack(side=tkinter.RIGHT)
        troopCharEntry.insert(tkinter.END, troopChar)
        battles_done_text = tkinter.StringVar()
        battles_done_text.set("Battles done: ")
        fightCountLabel = tkinter.Label(top, textvariable=battles_done_text)
        fightCountLabel.pack(side=tkinter.LEFT, padx=90)
        # Mainloop
        top.mainloop()

    except KeyboardInterrupt:
        print("Done")


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=Program)
    thread.start()

