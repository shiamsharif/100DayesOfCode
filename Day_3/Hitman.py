
print('''
*******************************************************************************
\ /    \ /     \ /    |/  | |  \|    \  \      / /         /\         \  \   \/
| |    | |     | |        | |        |\  \    // |        /. \        ||\ \  ||
| |____| |     | |        | |        ||\  \  //| |       // \ \       || \ \ ||
| |    | |     | |        | |        || \  \// | |      //___\ \      ||  \ \||
| |    | |     | |        | |        ||  \  /  | |     //     \ \     ||   \  |
/_\    /_\     /_\        /_\       /_\   \/   /_\    /_\     /__\   /__\   \_|

                                    /|
                                    \\  \`.
    _      _   _   _           ,'/  ||   ) `.                _        _
   |_) |  / \ / \ | \        ,' (   //,-'_,-'    ,   |\  /| / \ |\ | |_ \ /
   |_) |_ \_/ \_/ |_/  .    `-._`-.  |  (_____,-'/   | \/ | \_/ | \| |_  |
                       \`-._____)  | | ,-'-.    /
                        \    ,-'-. | |/     ) ,'
                         `. (     \|     _,','
                           `.`._

*******************************************************************************
''')
print("Welcome to HITMAN BLOOD MONEY.")
print("Your mission is to killed The President of Israle.")

choice1 = input('Landing from the helicopter ON president house by using "ROPE" or "PARACHUTE". == ').upper()

if choice1 == "ROPE":
    choice2 = input('which arms are you used to kill PGR Rengers, "Desert_Eagle_With_Suppressor for DES" or " Screwdriver" or "Ak-47" == ').upper()
    if choice2 == "DES":
        choice3 = input('which arms are you used to kill PGR Rengers, "Desert_Eagle_With_Suppressor for DES" or " Screwdriver" or "Modern Lethal Syringe for MLS" == ').upper()
        if choice3 == "Screwdriver":
            print("President are Extremly injured but still alive. Misson Failed.")
        elif choice3 == "DES":
            print("Game Over.")
        elif choice3 == "MLS":
            print( '''President are killed and You Win the game!
                                    
                        .-""""-.
                       / j      \
                      :.d;       ;
                      $$P        :
           .m._       $$         :
          dSMMSSSss.__$$b.    __ :
         :MMSMMSSSMMMSS$$$b  $$P ;
         SMMMSMMSMMMSSS$$$$     :b
        dSMMMSMMMMMMSSMM$$$b.dP SSb.
       dSMMMMMMMMMMSSMMPT$$=-. /TSSSS.
      :SMMMSMMMMMMMSMMP  `$b_.'  MMMMSS.
      SMMMMMSMMMMMMMMM \  .'\    :SMMMSSS.
     dSMSSMMMSMMMMMMMM  \/\_/; .'SSMMMMSSSm
    dSMMMMSMMSMMMMMMMM    :.;'" :SSMMMMSSMM;
  .MMSSSSSMSSMMMMMMMM;    :.;   MMSMMMMSMMM;
 dMSSMMSSSSSSSMMMMMMM;    ;.;   MMMMMMMSMMM
:MMMSSSSMMMSSP^TMMMMM     ;.;   MMMMMMMMMMM
MMMSMMMMSSSSP   `MMMM     ;.;   :MMMMMMMMM;
"TMMMMMMMMMM      TM;    :`.:    MMMMMMMMM;
   )MMMMMMM;     _/\\    :`.:    :MMMMMMMM
  d$SS$$$MMMb.  |._\\\   :`.:     MMMMMMMM
  T$$S$$$$$$$$$$m;O\\\\"-;`.:_.-  MMMMMMM;
 :$$$$$$$$$$$$$$$b_l./\\ ;`.:    mMMSSMMM;
 :$$$$$$$$$$$$$$$$$$$./\\;`.:  .$$MSMMMMMM
  $$$$$$$$$$$$$$$$$$$$. \\`.:.$$$$SMSSSMMM;
  $$$$$$$$$$$$$$$$$$$$$. \\.:$$$$$SSMMMMMMM
  :$$$$$$$$$$$$$$$$$$$$$.//.:$$$$SSSSSSSMM;
  :$$$$$$$$$$$$$$$$$$$$$$.`.:$$SSSSSSSMMMP
   $$$$$$$$$;"^$J "^$$$$;.`.$$P  `SSSMMMM
   :$$$$$$$$$       :$$$;.`.P'..   TMMM$$b
   :$$$$$$$$$;      $$$$;.`/ c^'   d$$$$$S;
   $$$$$S$$$$;      '^^^:_d$g:___.$$$$$$SSS
   $$$$SS$$$$;            $$$$$$$$$$$$$$SSS;
  :$$$SSSS$$$$            : $$$$$$$$$$$$$SSS
  :$P"TSSSS$$$            ; $$$$$$$$$$$$$SSS;
  j    `SSSSS$           :  :$$$$$$$$$$$$$SS$
 :       "^S^'           :   $$$$$$$$$$$$$S$;
 ;.____.-;"               "--^$$$$$$$$$$$$$P
 '-....-"  Shiam                  ""^^T$$$$P"
                  ''')
        else: 
            print("You are kill by PGR(President Guard Regiment). Misson Failed.")
    else:
        print("You are Caught by PGR(President Guard Regiment). Misson Failed.")
else:
    print("You are kill by PGR(President Guard Regiment).Game Over.")