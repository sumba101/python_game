shield=False
start_col=0
boost_speed=0
boost_end_time=-1
start_time=0
score=0
time_left=0
lives=3
state='r'
hangtime=1

hero=[" O   ","<\===","/ \  "]

villain=["            ______________               ","      ,===:'.,            `-._           ","           `:.`---.__         `-._       ",
        "              `:.     `--.         `.    ","               \.        `.         `.   ","       (,,(,    \.         `.   ____,-`.,",
         "    (,'     `/   \.   ,--.___`.'         ",",  ,'  ,--.  `,   \.;'         `         "," `{D, {    \  :    \;                    "
         "   V,,'    /  /    //                    ","   |;;    /  ,' ,-//.    ,---.      ,    ","   \;'   /  ,' /  _  \  /  _  \   ,'/    ",
        "         \   `'  / \  `'  / \  `.' /     ","          `.___,'   `.__,'   `.__,'      "
        ]

cloud=["   __   _   "," _(  )_( )_ ","(_   _    _)","  (_) (__)  "]

#co ordinates of the hero
hero_y=-1
hero_x=-1
#2 for vertical
#4 for across

#co ordinates of the villain
villain_y=5
villain_x=3
#40 across offset
#13 vertical offset

height=-1
width=-1
frame_width=-1

result=0 #for checking if game is won or lost

villain_life=4