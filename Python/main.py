import breakScript as brk
import playVid as PV
import multiprocessing as mult
import pokemon as pok

testData = {"rfid": "123456789","username": "kidNamedKid", "info" : {"pokemon_name": "", "pokemon_xp": 0, "attack_xp": 0, "defense_xp": 0, "speed_xp": 0, "health_xp": 0, "pokemon_name": "raichu"}}

def mainLoop():


    
    event = mult.Event()
    defProc = mult.Process(target=PV.instructionsVid, args=(event,))
    defProc.start()

    # Database check with RFID and return all relevant data
    # TODO RFIDInfo = DatabaseData() (JEWSKY)
    RFIDData = testData

    RFIDInfo = RFIDData["info"]


    # Wait Until RFID Read
    defProc.join()


    # input("Press Enter to continue...")

    pBreakBeam = mult.Process(target=brk.mainFunc)
    pVid = mult.Process(target=PV.chooseVideo, args=(event, RFIDInfo))

    eventMain = mult.Event()
    pBreakBeam.start()
    pVid.start()

    pBreakBeam.join()
    eventMain.set()
    pVid.join()

    breakBeam = pBreakBeam.exitcode
    newPok = pVid.exitcode
    
    if RFIDInfo["pokemon_name"] == True:
        RFIDInfo["pokemon_xp"] += 20
        if (RFIDInfo["pokemon_name"] not in pok.finalPok):
            if breakBeam ==3 or ["pokemon_xp"] > pok.FirstEvol:
                RFIDInfo["pokemon_name"] = pok.evolutionDict[RFIDInfo["pokemon_name"]]
                RFIDInfo["attack_xp"] += pok.evolutionStatBoost[RFIDInfo["pokemon_name"]][0]
                RFIDInfo["defense_xp"] += pok.evolutionStatBoost[RFIDInfo["pokemon_name"]][1]
                RFIDInfo["speed_xp"] += pok.evolutionStatBoost[RFIDInfo["pokemon_name"]][3]
                RFIDInfo["health_xp"] += pok.evolutionStatBoost[RFIDInfo["pokemon_name"]][4]
                if RFIDInfo["pokemon_name"] in pok.finalPok:
                    RFIDInfo["pokemon_xp"] = pok.LastEvol
                elif RFIDInfo["pokemon_name"] not in pok.finalPok:
                    RFIDInfo["pokemon_xp"] = pok.FirstEvol
            else:
                if breakBeam == 1:
                    RFIDInfo["attack_xp"] +=pok.attackInc
                elif breakBeam ==2:
                    RFIDInfo["defense_xp"] +=pok.defenseInc
                elif breakBeam ==4:
                    RFIDInfo["speed_xp"] +=pok.speedInc
                elif breakBeam ==5:
                    RFIDInfo["health_xp"] +=pok.healthInc

        elif (RFIDInfo["pokemon_name"] in pok.finalPok):
            if breakBeam == 3:
                RFIDInfo["attack_xp"] += pok.evolutionStatBoost[RFIDInfo["pokemon_name"]][0]
                RFIDInfo["defense_xp"] += pok.evolutionStatBoost[RFIDInfo["pokemon_name"]][1]
                RFIDInfo["speed_xp"] += pok.evolutionStatBoost[RFIDInfo["pokemon_name"]][3]
                RFIDInfo["health_xp"] += pok.evolutionStatBoost[RFIDInfo["pokemon_name"]][4]
            elif breakBeam ==1:
                RFIDInfo["attack_xp"] +=pok.attackInc
            elif breakBeam ==2:
                RFIDInfo["defense_xp"] +=pok.defenseInc
            elif breakBeam ==4:
                RFIDInfo["speed_xp"] +=pok.speedInc
            elif breakBeam ==5:
                RFIDInfo["health_xp"] +=pok.healthInc
    else: # new
        if breakBeam ==3:
            RFIDInfo["pokemon_name"] = newPok[breakBeam]
            # TODO Pokemon Speed, Attack, Defense, Health, XP attributes Set
        else:
            # TODO Pokemon Speed, Attack, Defense, Health, XP attributes Set
            if breakBeam == 1:
                RFIDInfo["pokemon_name"] = "balbasaur"
                
            elif breakBeam ==2:
                RFIDInfo["pokemon_name"] = "squirtle"
            elif breakBeam ==4:
                RFIDInfo["pokemon_name"] = "charmander"
            elif breakBeam ==5:
                RFIDInfo["pokemon_name"] = "pikachu"
        RFIDInfo["attack_xp"] = pok.baseStats[RFIDInfo["pokemon_name"]][0]
        RFIDInfo["defense_xp"] = pok.baseStats[RFIDInfo["pokemon_name"]][1]
        RFIDInfo["speed_xp"] = pok.baseStats[RFIDInfo["pokemon_name"]][2]
        RFIDInfo["health_xp"] = pok.baseStats[RFIDInfo["pokemon_name"]][3]
        RFIDInfo["pokemon_xp"] = pok.baseStats[RFIDInfo["pokemon_name"]][4]

# TODO write code to display pokemon you received for x ammount of seconds
# The above will likely use concurrency 

# TODO Write Code to update database with RFIDInfo : Jewsky Code


if __name__ == "__main__":
    while True:
        mainLoop()