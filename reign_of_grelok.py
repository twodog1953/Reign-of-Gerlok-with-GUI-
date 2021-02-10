# reign of Grelok, by Klaus Song, 2020.7.6

import numpy as np
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.title('Reign of Grelok')

# items
sword = 'Rusty Sword'
flask = 'Drinking Flask'
head = 'A rotten zombie head'
key = 'A big, heavy brass key'
water_flask = 'A drinking flask filled with blessed water'
gem = 'A rough gemstone'
shard = 'The shard from the original gemstone. '
chaff = 'The chaff from the original gemstone.'
en_sword = 'An enchanted weapon to defeat Grelok. '

# the inventory system
inv_bag = [sword, flask]

mov_mid = "You are now in the middle part of the map. "
mov_north = "You are now in the north part of the map. "
mov_south = "You are now in the south part of the map. "
mov_west = "You are now in the west part of the map. "
mov_east = "You are now in the east part of the map. "
mov_warning = "You can't move in that direction. "

zombie_killed = False
grelok_found = False

# current location: 0 is mid, 1=north, 2=south, 3=west, 4=east
current_loc = "mid"

bac_mid = 'You are standing in a wide plain. Foothills stretch to the north, where clouds gather around an ominous ' \
          'peak. A dirt path winds from a lonely chapel to the east, through the plains where you are standing, ' \
          'and south into a bustling town. Wispy mists gather over marshland in the west, where a thin tower stands ' \
          'alone in the bog. '
bac_north = 'You are on the craggy, windblasted face of a mountain. Stormclouds coil above the summit, pelting you ' \
            'and the sparse vegetation with torrential downpour. Far below, beyond the foothills, a wide plain ' \
            'stretches across the southern horizon. \n Gerlock is here, spewing heresies. '
bac_south = 'You are standing in the dusty market square of a quiet town. Many of the shops and homes lie abandoned, ' \
            'and the citizens that can be seen speak in hushed voices, casting furtive glances at the darkened ' \
            'skyline in the distanced north. The ringing of an anvil breaks the silence regularly, where a mustachioed ' \
            'blacksmith bends over his work in a nearby tent. \n The blacksmith is here, working. \n A priest is ' \
            'here, drinking. '
bac_west = 'You are standing on a narrow stone path in a dark marsh. Greasy bubbles float to the top of the ' \
           'bog-waters on either side and pop lazily. Spattering your legs with muck and slime. A short, stine tower ' \
           'squats here. No door is visible, and the stones are smooth and polished. A balcony juts out midway up the ' \
           'towers face. The heady smells of incense mix with nauseating stench of the swamp. The stone path unfurls ' \
           'eastward, towards a broad plain beyond the marshes. \n A wizard is here, gesticulating wildly from his ' \
           'balcony. '
bac_east_1 = 'You stand at the end of a dirt path, facing a small chapel. The succo walls are faded, many roof tiles ' \
             'are missing. The great oaken doors are locked. The congregation is nowhere tp be found. A small cemetery ' \
             'of the crooked headstones lies in the shadow of the cracked steeple. The dirt path winds westward through ' \
             'a great, featureless plain. \n A zombie totters aimlessly nearby. \n There is an open grave nearby. '
bac_east_2 = 'You stand at the end of a dirt path, facing a small chapel. The succo walls are faded, many roof tiles ' \
             'are missing. The great oaken doors are locked. The congregation is nowhere tp be found. A small cemetery ' \
             'of the crooked headstones lies in the shadow of the cracked steeple. The dirt path winds westward through ' \
             'a great, featureless plain. \n There is an open grave nearby. '


def clicked_north():
    global current_loc, grelok_found
    if grelok_found == False:
        if current_loc == "north" or current_loc == "west" or current_loc == "east":
            showinfo(title='Warning: ', message=mov_warning)
        elif current_loc == "mid":
            showinfo(message=mov_north)
            current_loc = "north"
            context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_north)
            act_but1.config(text='use sword Gerlok')
            act_but2.config(text='Investigate glinting object')
            act_but3.config(text=act_labels[2])
            act_but4.config(text='check inventory')
        elif current_loc == "south":
            showinfo(message=mov_mid)
            current_loc = "mid"
            context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_mid)
            act_but1.config(text=act_labels[0])
            act_but2.config(text=act_labels[1])
            act_but3.config(text=act_labels[2])
            act_but4.config(text='check inventory')
    else:
        showinfo(message='You cannot move now, as Grelok is about to attack you! ')


def clicked_south():
    global current_loc, grelok_found, act_but1, act_but2
    if grelok_found == False:
        if current_loc == "south" or current_loc == "west" or current_loc == "east":
            showinfo(title='Warning: ', message=mov_warning)
        elif current_loc == "mid":
            showinfo(message=mov_south)
            current_loc = "south"
            context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_south)
            act_but1.config(text='speak with blacksmith')
            act_but2.config(text='speak with priest')
            act_but3.config(text=act_labels[2])
            act_but4.config(text='check inventory')
        elif current_loc == "north":
            showinfo(message=mov_mid)
            current_loc = "mid"
            context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_mid)
            act_but1.config(text=act_labels[0])
            act_but2.config(text=act_labels[1])
            act_but3.config(text=act_labels[2])
            act_but4.config(text='check inventory')
    else:
        showinfo(message='You cannot move now, as Grelok is about to attack you! ')


def clicked_west():
    global current_loc, grelok_found
    if grelok_found == False:
        if current_loc == "north" or current_loc == "south" or current_loc == "west":
            showinfo(title='Warning: ', message=mov_warning)
        elif current_loc == "mid":
            showinfo(message=mov_west)
            current_loc = "west"
            context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_west)
            act_but1.config(text='talk to the wizard')
            act_but2.config(text=act_labels[1])
            act_but3.config(text=act_labels[2])
            act_but4.config(text='check inventory')
        elif current_loc == "east":
            showinfo(message=mov_mid)
            current_loc = "mid"
            context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_mid)
            act_but1.config(text=act_labels[0])
            act_but2.config(text=act_labels[1])
            act_but3.config(text=act_labels[2])
            act_but4.config(text='check inventory')
    else:
        showinfo(message='You cannot move now, as Grelok is about to attack you! ')


def clicked_east():
    global current_loc, grelok_found
    if grelok_found == False:
        if current_loc == "north" or current_loc == "south" or current_loc == "east":
            showinfo(title='Warning: ', message=mov_warning)
        elif current_loc == "mid":
            showinfo(message=mov_east)
            current_loc = "east"
            if head not in inv_bag:
                context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_east_1)
                act_but1.config(text='use sword zombie')
            else:
                context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_east_2)
                act_but1.config(text=act_labels[0])
            act_but2.config(text='check grave')
            if key in inv_bag:
                act_but3.config(text='check chapel')
            elif key not in inv_bag:
                act_but3.config(text=act_labels[2])
        elif current_loc == "west":
            showinfo(message=mov_mid)
            current_loc = "mid"
            context.config(text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_mid)
            act_but1.config(text=act_labels[0])
            act_but2.config(text=act_labels[1])
            act_but3.config(text=act_labels[2])
            act_but4.config(text='check inventory')
    else:
        showinfo(message='You cannot move now, as Grelok is about to attack you! ')


def action_1():
    if current_loc == 'east':
        # use sword zombie
        global zombie_killed, act_but1
        if not zombie_killed:
            showinfo(message='Your blow knocks the zombie into a grave. ')
            zombie_killed = True
            act_but1.config(text='action1')
        else:
            showinfo(message='? \n Theres no zombie here now. ')
    if current_loc == 'south':
        # speak with blacksmith
        if shard not in inv_bag and chaff not in inv_bag and en_sword not in inv_bag:
            showinfo(message='Your eyes water from smoke and smarmy heat inside the tent. The huge man swipes sweat from '
                        'his bald head and looks up from his work. \n "Theres no shortage of work to be done with '
                        'Gerlock scaring everyone witless. Leave me to filling my orders, stranger." With that, '
                        'the blacksmith dismisses you from his tent and douses a hot blade in water, hissing with '
                        'steam. ')
        elif shard in inv_bag and chaff in inv_bag:
            showinfo(message='The blacksmith regards you gruffly and is about to dismiss you when you produce the '
                          'polished gemstone from your bag. He sets his hammer aside and twirls his moustache. \n "A '
                          'right fine stone, that is. " He says, admiring the faceted stone, "what would you be '
                          'needing then? " \n Following your careful instructions, the smithy re-forges your rusty '
                          'sword with the magical shard at the center of the blade. ')
            inv_bag.remove(sword)
            inv_bag.remove(chaff)
            inv_bag.remove(shard)
            inv_bag.append(en_sword)
    if current_loc == 'west':
        if gem not in inv_bag and shard not in inv_bag and en_sword not in inv_bag:
            showinfo(
                message='The wizard beckons wildly at you from his balcony. "You are here, you ve finally arrived! " '
                        'He exclaims. After a awkward silence, he jabs an excited finger into a crystal ball, '
                        'nearly knocking it into the bog. \n "Ive seen, you see. You are the one to defeat Gerlock. '
                        'Hoo-hoo!" The little man hops onto the railing, spinning a pirouette. "Now the time is come '
                        'to play my part. Toss up the gem!" \n The wizards brow furrows. "Got things a bit out of '
                        'order, have I? Come back when you have got a powerful gemstone. Soon - I have never got to '
                        'fulfill a prophecy before! "')
        elif gem in inv_bag:
            showinfo(message='"Hoo-hoo! The slayer of Grelok approaches, raw stone in hand, just as Ive seen! " The '
                             'wizards pointy hat bobs excitedly as he points a finger at you. Suddenly, a pale orange '
                             'arc of light extends from the knobby finger and draws the gemstone from your bag before '
                             'you can react. The gemstone halts and hovers in the air before the wizards nose. \n '
                             '"Essence be true, powers renew, Fatty-Hoo-Do! " With that, he slaps the hoovering '
                             'stone, smashing it against the smooth stone of the tower. In a burst of light, '
                             'the stone splits into two, and one lands in each outstretched palm of the hopping '
                             'little wizard. \n "Shard for the sword. Wrap her in iron and she will find Greloks '
                             'black heart for you. Take the chaff too. You will need payment for a smith to forge the '
                             'weapon. " He tosses the stones down which you leap forward to catch safely. ')
            inv_bag.remove(gem)
            inv_bag.append(shard)
            inv_bag.append(chaff)
        else:
            showinfo(message='The wizard has returned to his tower.')
    global grelok_found
    if current_loc == 'north' and grelok_found == False:
    # fight
        if en_sword not in inv_bag:
            showinfo(message='When you draw your sword, Grelok lowers his great horned head and bellows laughter in '
                             'your face. You grit your teeth and swing a mighty two-handed blow, but your sword '
                             'cannot penetrate Greloks block, as its too weak. Greloks laughs heartily, '
                             'and is about to end your life with his giant dark claws. ')
            grelok_found = True
            if water_flask in inv_bag:
                act_but3.config(text='use the water flask')
            elif water_flask not in inv_bag:
                showinfo(message='You died. Now Grelok would be act his evil deeds without anyone to stop him. ')
                showinfo(message='THE END. \n (Thank you for playing! )')
                root.quit()
        elif en_sword in inv_bag:
            showinfo(message='When you draw your sword, Grelok lowers his great horned head and bellows laughter in '
                             'your face. You grit your teeth and swing a mighty two-handed blow, the magical blade '
                             'ringing clearly, even amid the tumult of throaty crackling. \n You swing the sword so '
                             'fiercely, it escapes your grip and hurtles into the open maw of the monstrosity, '
                             'lost from sight in the arid darkness  of Greloks throat. You step back as Grelok jerks '
                             'his mouth shut and stands upright. He is still for a moment, then starts clawing at his '
                             'neck. Muffled, a ringing can be heard as if from a great distance. \n Suddenly, '
                             'Greloks chest bursts in a fount of viscous, green blood. The ringing can be heard '
                             'clearly now, and is as thick lifeblood oozes around the protruding tip of the magic '
                             'sword, the stormclouds swirling the peak are already clearing. Grelok is defeated! ')
            showinfo(message='THE END. \n (Thank you for playing! )')
            root.quit()


def action_2():
    if current_loc == 'east':
        # check the grave
        if head in inv_bag:
            showinfo(message='You peer into the open grave. There is a deep, empty grave in the cemetery. There"s '
                             'nothing in there other than a headless zombie body. ')
        if head not in inv_bag and zombie_killed == True:
            showinfo(message='You peer into the open grave. There is a deep, empty grave in the cemetery. Several '
                             'bloated rats and a zombie corpse float in a foot of filthy water at the bottom. Don"t '
                             'fall in! \n A grotesque zombie head is stuck on a root near the top of the grave. You '
                             'bag the horrific trophy das proof of your deed. ')
            inv_bag.append(head)
        if head not in inv_bag and zombie_killed == False:
            showinfo(message='You peer into the open grave. There is a deep, empty grave in the cemetery. There"s '
                             'nothing in there. ')
    if current_loc == 'south':
        if key not in inv_bag:
            # speak with priest
            if head not in inv_bag:
                showinfo(message='The priest drunkenly curses the undead who have defiled his church. "The curse of '
                                 'Gerlock raised the dead from the cemetery and desecrate my church. If you can put kill '
                                 'that zombie for me, I shall grant you access to my church and anything inside would be '
                                 'yours to grab. "')
            if head in inv_bag:
                showinfo(message='The priest drunkenly curses the undead who have defiled his church. You present him '
                                 'with the decapitated zombie head from your bag. \n "Praise you! ", he hiccups. "Perhaps '
                                 'Gerlocks influence isnt so strong! ". With that, he turns his decanter over on the head '
                                 'and tosses into a fireplace, where it bursts into purple flame and burns up almost '
                                 'instantly. \n "I must gather the faithful. " He presses a brass key into your palm, '
                                 '"Please, help yourself to what little may be of use at my chapel. "')
                inv_bag.append(key)
        elif key in inv_bag:
            showinfo(message='The priest is drinking water, poring over a thick, leatherbound volume connected by a '
                          'thick leather thong to his neck. He notices you only when you have come very close. \n '
                          '"Ah, good friend! Have you gone ahead to open the chapel? My body still aches with drink, '
                          'Im afraid, but soon  will gather the congregation and return myself. "')
    global grelok_found
    if current_loc == 'north' and grelok_found == False:
        if gem not in inv_bag and en_sword not in inv_bag and shard not in inv_bag:
            # take gemstone
            showinfo(message='You take a rough gemstone from the rocks. ')
            inv_bag.append(gem)
        else:
            # already have gemstone
            showinfo(message='Theres nothing special here anymore. ')


def action_3():
    global grelok_found
    # check chapel
    if current_loc == 'east' and key in inv_bag and flask in inv_bag:
        showinfo(message='Dust motes hang lazily in the shafts of colored light stretching across te chapel from peaked '
                 'windows. The pews, pulpit, and everything else are covered in a fine mist. There os a very deep '
                 'stone cistern near the entrance. It is full to the brim withblessed water. \n There is more than '
                 'enough water here to fill your tiny flask. ')
        inv_bag.remove(flask)
        inv_bag.append(water_flask)
    # use flask in danger
    if current_loc == 'north' and grelok_found == True:
        global act_but3
        showinfo(message='You used the magical water in your trusty flask. Suddenly, you body becomes '
                         'invisible and merges into the surrounding land, confusing the Grelok and allowing '
                         'you to escape his fierce strike without a scratch. ')
        act_but3.config(text=act_labels[2])
        grelok_found = False


def action_4():
    # always check the inventory for this button
    inv_now = ''
    global inv_bag
    for items in inv_bag:
        inv_now += items + '\n'
    showinfo(message='You open the bag... \n' + 'You have: \n \n' + inv_now)


context = Label(root, text='You are currently in the ' + current_loc + ' part of the map. \n' + bac_mid, wraplength=500,
                width=80)
context.grid(row=0, column=0, columnspan=2)
mov_label = Label(root, text='What"s your next move?', width=80, wraplength=500)
mov_label.grid(row=1, column=0, columnspan=2)

labels = [['go north'],
          ['go south'],
          ['go west '],
          ['go east ']]

act_labels = ['action1', 'action2', 'action3', 'action4']

# for r in range(2, 6):
#     for c in range(1):
#         label = Button(root,
#                        relief=RAISED,
#                        padx=10,
#                        text=labels[r - 2][c],
#                        command=clicked,
#                        width=20,
#                        height=2,
#                        borderwidth=5)
#
#         label.grid(row=r, column=c)

but_north = Button(root, relief=RAISED, padx=10, text=labels[0][0], command=clicked_north, width=20, height=2,
                   borderwidth=5).grid(row=2, column=0)
but_south = Button(root, relief=RAISED, padx=10, text=labels[1][0], command=clicked_south, width=20, height=2,
                   borderwidth=5).grid(row=3, column=0)
but_west = Button(root, relief=RAISED, padx=10, text=labels[2][0], command=clicked_west, width=20, height=2,
                  borderwidth=5).grid(row=4, column=0)
but_east = Button(root, relief=RAISED, padx=10, text=labels[3][0], command=clicked_east, width=20, height=2,
                  borderwidth=5).grid(row=5, column=0)

act_but1 = Button(root, relief=RAISED, padx=10, text=act_labels[0], command=action_1, width=20, height=2,
                  borderwidth=5)
act_but1.grid(row=2, column=1)
act_but2 = Button(root, relief=RAISED, padx=10, text=act_labels[1], command=action_2, width=20, height=2,
                  borderwidth=5)
act_but2.grid(row=3, column=1)
act_but3 = Button(root, relief=RAISED, padx=10, text=act_labels[2], command=action_3, width=20, height=2,
                  borderwidth=5)
act_but3.grid(row=4, column=1)
act_but4 = Button(root, relief=RAISED, padx=10, text='check inventory', command=action_4, width=20, height=2,
                  borderwidth=5)
act_but4.grid(row=5, column=1)

root.mainloop()

# a = np.ones(100)
# b = input('Input the numba: ')
# for i in range(len(a)):
#     a[i] = test_function.test(a[i]*i*float(b))
# print(a)
