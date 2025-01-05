import sys,pygame,time,Oofff

# room loader


# maintenance = 0
# universal_keys = 1
# gasoline = 2
# physics_keys = 3
# elevator_keys = 4

def loadrooms():

    backbuttonrect = [325,565,150,40]
    roomslist=[]

    room = Oofff.Room([0,'room0_b2_203',[backbuttonrect+[19,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([1,'room1_b2_alleyway_dark',[backbuttonrect+[23,-1,-1,-1],
                                                   [350,65,142,409,4,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([2,'room2_level2_hallwayright',[backbuttonrect+[47,-1,-1,-1],
                                                   [334,126,169,288,47,-1,-1,-1],
                                                      [620,44,94,430,51,-1,1,-1],
                                                      [551,114,32,346,43,-1,1,-1]]])
    roomslist.append(room)



    room = Oofff.Room([3,'room3_0_b2_allyway_gascans',[backbuttonrect+[4,-1,-1,-1],
                                                       [223,127,185,155,3,1,-1,2]]],
                      [3,'room3_1_b2_allyway_gascans',[backbuttonrect+[4,-1,-1,-1]]])
                                                
    roomslist.append(room)

    room = Oofff.Room([4,'room4_b2_allyway',[backbuttonrect+[1,-1,-1,-1],
                                             [303,306,89,119,3,-1,-1,-1],
                                             [373,139,76,181,31,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([5,'room5_b2_art',[backbuttonrect+[34,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([6,'room6_b2_atdoor',[backbuttonrect+[49,-1,-1,-1],
                                            [16,273,82,130,28,-1,-1,-1],
                                            [609,255,90,88,29,-1,-1,-1],
                                            [262,198,296,139,23,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([7,'room7_b2_atmrgordans',[backbuttonrect+[36,-1,-1,-1],
                                                 [16,86,172,448,40,-1,1,-1],
                                                 [401,161,103,172,49,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([8,'room8_b2_balcony',[backbuttonrect+[33,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([9,'room9_b2_bleachers_gascan',[backbuttonrect+[11,-1,-1,-1]]])
    roomslist.append(room)

                                                      # x , y  ,w  ,l,nr,ns,iu,ig
    room = Oofff.Room([10,'room10_b2_bleachers_stairs',[[98,81,152,392,15,-1,-1,-1],
                                                       backbuttonrect+[16,-1,-1,-1],
                                                       [505,43,273,540,11,-1,-1,-1]]])
    
    roomslist.append(room)
    
    room = Oofff.Room([11,'room11_b2_bleachers',[backbuttonrect+[10,-1,-1,-1],
                                               [211,158,169,264,9,-1,-1,-1]]])
    roomslist.append(room)
    
    room = Oofff.Room([12,'room12_0_physics_cabinet_closed',[backbuttonrect+[27,-1,1,-1],
                                                            [248,36,284,492,12,1,3,-1]]],
                     [12,'room12_1_b2_cabinet_open',[backbuttonrect+[27,-1,1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([13,'room13_b2_generator',[backbuttonrect+[31,-1,-1,-1],
                                               [492,331,98,101,14,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([14,'room14_b2_genertor_gascap',[backbuttonrect+[13,-1,-1,-1],
                                                       [264,212,300,236,14,1,2,5]]],
                      [14,'room14_b2_genertor_gascap',[backbuttonrect+[13,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([15,'room15_b2_gym_storage',[backbuttonrect+[10,-1,-1,-1],
                                                   [164,184,94,112,10,1,-1,2]]],
                      [15,'room15_b2_gym_storage',[backbuttonrect+[10,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([16,'room16_b2_gym',[backbuttonrect+[19,-1,-1,-1],
                                          [617,213,115,110,10,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([17,'room17_b2_hallway_doors',[backbuttonrect+[32,-1,-1,-1],
                                                     [60,8,172,542,25,-1,1,-1],
                                                     [403,104,155,350,20,-1,1,-1],
                                                     [618,49,72,489,27,-1,1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([18,'room18_b2_hallway3',[backbuttonrect+[19,-1,-1,-1],
                                                [311,140,121,265,22,-1,1,-1],
                                                [512,141,45,368,30,-1,1,-1]]])
    
    roomslist.append(room)

    room = Oofff.Room([19,'room19_b2_lockers',[backbuttonrect+[29,-1,-1,-1],
                                               [737,123,59,393,18,-1,-1,-1],
                                               [598,122,107,256,0,-1,1,-1],
                                               [0,156,118,242,16,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([20,'room20_b2_marmar',[backbuttonrect+[17,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([21,'room21_b2_mrcampbell',[backbuttonrect+[34,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([22,'room22_b2_mrfluge',[backbuttonrect+[18,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([23,'room23_b2_mrveech',[backbuttonrect+[6,-1,-1,-1],
                                               [4,173,280,262,29,-1,-1,-1],
                                               [723,237,29,114,1,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([24,'room24_b2_music',[backbuttonrect+[33,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([25,'room25_b2_myanmarstudies',[backbuttonrect+[17,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([26,'room26_b2_physics_desk',[backbuttonrect+[27,-1,1,-1],
                                                    [357,340,219,180,80,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([27,'room27_b2_physics',[backbuttonrect+[17,-1,-1,-1],
                                               [284,165,75,134,12,-1,-1,-1],
                                               [609,207,167,185,26,-1,-1,-1]]])
    roomslist.append(room)
                    
                           #state pics haven't been taken
    room = Oofff.Room([28,'room28_1_b2_securitydesk',[backbuttonrect+[6,-1,-1,-1],
                                                    [342,249,248,153,28,1,-1,1]]],
                      [28,'room28_1_b2_securitydesk',[backbuttonrect+[6,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([29,'room29_b2_stairs',[backbuttonrect+[23,-1,-1,-1],
                                              [164,167,159,140,19,-1,-1,-1],
                                              [487,26,312,490,32,-1,-1,-1]]])
    roomslist.append(room)
                            #add gas later
    room = Oofff.Room([30,'room30_b2_storage',[backbuttonrect+[18,-1,-1,-1]]])

    roomslist.append(room)

    room = Oofff.Room([31,'room31_b2_togenerator',[backbuttonrect+[4,-1,-1,-1],
                                                  [208,39,50,295,13,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([32,'room32_b2_upperstairs',[backbuttonrect+[29,-1,-1,-1],
                                                   [495,97,125,301,25,-1,1,-1],
                                                   [40,149,232,216,34,-1,-1,-1],
                                                   [640,141,132,251,17,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([33,'room33_b2_upstairshallway',[backbuttonrect+[34,-1,-1,-1],
                                                       [434,82,41,320,24,-1,1,-1],
                                                       [47,205,222,299,8,-1,-1,-1]]])
                    
    roomslist.append(room)

    room = Oofff.Room([34,'room34_b2_upstairshallway2',[backbuttonrect+[32,-1,-1,-1],
                                                       [166,182,74,206,5,-1,1,-1],
                                                       [711,134,29,300,21,-1,1,-1],
                                                        [2,159,80,210,33,-1,-1,-1]]])
                    
    roomslist.append(room)

    
                
    room = Oofff.Room([35,'room35_elevator',[
                                               [519,121,31,41,65,-1,-1,-1],
                                               [516,236,33,36,57,-1,-1,-1],
                                               [515,182,33,39,69,-1,-1,-1],
                                               [515,289,29,36,44,-1,-1,-1],
                                               [515,334,33,43,36,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([36,'room36_level0_atrium',[backbuttonrect+[41,-1,-1,-1],
                                               [349,219,410,200,7,-1,-1,-1]
                                               ]])
    roomslist.append(room)

    room = Oofff.Room([37,'room37_0_level0_maintenance',[backbuttonrect+[49,-1,-1,-1],
                                                         [480,161,34,59,37,1,-1,0]]
                                              ],
                      [37,'room37_1_level0_maintenance',[backbuttonrect+[49,-1,-1,-1]
                                              ]])
    roomslist.append(room)


    room = Oofff.Room([38,'room38_stairwell_level1',[backbuttonrect+[44,-1,-1,-1],
                                               [592,3,194,526,44,-1,-1,-1],
                                               [3,319,149,276,64,-1,-1,-1],
                                               [227,422,244,147,41,-1,-1,-1]]])
    roomslist.append(room)
                      
    room = Oofff.Room([39,'room39_0_level0_mrgordan_key',[backbuttonrect+[40,-1,-1,-1],
                                               [350,255,102,76,39,1,-1,4],
                                                ]],
                       [39,'room39_1_level0_mrgordan_key_gone',[backbuttonrect+[40,-1,-1,-1]]
                       ])
                      
    roomslist.append(room)

    room = Oofff.Room([40,'room40_level0_mrgordan',[backbuttonrect+[36,-1,-1,-1],
                                                    [368,255,337,14,39,-1,-1,-1]]])
    roomslist.append(room)
    
    room = Oofff.Room([41,'room41_level0_stairwell',[backbuttonrect+[38,-1,-1,-1],
                                                    [500,217,201,229,36,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([42,'room42_level1_computer',[backbuttonrect+[43,-1,1,-1]]
                                                    ])
    roomslist.append(room)
    


    room = Oofff.Room([43,'room43_level1_computerlab',[backbuttonrect+[47,-1,-1,-1],
                                                    [347,211,36,28,42,-1,-1,-1]]])
    roomslist.append(room)
    
    room = Oofff.Room([44,'room44_level1_hall1',[backbuttonrect+[46,-1,-1,-1],
                                                    [58,182,87,297,35,-1,6,-1],
                                                       [407,139,277,176,45,-1,-1,-1],
                                                       [187,201,38,224,38,-1,-1,-1],
                                                       [695,168,60,188,47,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([45,'room45_level1_hall2',[backbuttonrect+[47,-1,-1,-1],
                                                    [135,228,43,138,46,-1,-1,-1],
                                                       [201,252,230,108,44,-1,-1,-1],
                                                       [590,204,48,212,35,-1,6,-1],
                                                 [705,197,74,324,38,-1,-1,-1],
                                                 [25,251,107,154,48,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([46,'room46_level1_hallwayleft',[backbuttonrect+[44,-1,-1,-1],
                                                    [79,129,56,369,54,-1,1,-1],
                                                       [133,143,40,276,52,-1,1,-1],
                                                       [681,33,118,502,55,-1,1,-1],
                                                       [205,156,167,242,44,-1,-1,-1]]])
    roomslist.append(room)


    room = Oofff.Room([47,'room47_level1_hallwayright',[backbuttonrect+[45,-1,-1,-1],
                                                    [361,337,111,71,45,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([48,'room48_0_level1_lockerclosed',[backbuttonrect+[45,-1,-1,-1],
                                                    [522,130,207,403,48,1,-1,-1]]],
                      [48,'room48_1_level1_lockeropen',[backbuttonrect+[45,-1,-1,-1],
                                                       [522,130,207,403,48,0,-1,-1]]])

    roomslist.append(room)
    
    room = Oofff.Room([49,'room49_0_tob2_closed',[backbuttonrect+[7,-1,-1,-1],
                                                    [465,125,146,450,37,-1,-1,-1],
                                                  [0,65,419,510,49,1,0,-1]]],
                      [49,'room49_1_tob2_open',[backbuttonrect+[7,-1,-1,-1],
                                                [465,125,146,450,37,-1,-1,-1],
                                                [0,65,419,510,6,-1,-1,-1]]])
                      
    roomslist.append(room)

    room = Oofff.Room([50,'room50_level1_lockers',[backbuttonrect+[45,-1,-1,-1],
                                               [329,68,166,316,45,-1,-1,-1],
                                                   [521,97,62,446,43,-1,1,-1],
                                                   [615,36,111,524,52,-1,1,-1]]])
    roomslist.append(room)

                      
    room = Oofff.Room([51,'room51_level1_mrbob',[backbuttonrect+[50,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([52,'room52_level1_mrthayer',[backbuttonrect+[46,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([53,'room53_level1_msanna_dead',[backbuttonrect+[54,-1,1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([54,'room54_level1_msanna',[backbuttonrect+[46,-1,-1,-1],
                                                  [484,230,136,108,53,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([55,'room55_level1_mslea',[backbuttonrect+[46,-1,-1,-1]]])
    roomslist.append(room)

    
    room = Oofff.Room([56,'room56_level2_hallway1',[backbuttonrect+[58,-1,-1,-1],
                                               [8,142,118,316,35,-1,6,-1],
                                                   [132,146,31,272,64,-1,-1,-1],
                                                   [369,175,207,215,57,-1,-1,-1],
                                                    [625,171,88,226,2,-1,-1,-1]]])
    roomslist.append(room)

    
    room = Oofff.Room([57,'room57_level2_hallway2',[backbuttonrect+[2,-1,-1,-1],
                                               [713,170,82,357,64,-1,-1,-1],
                                                   [617,196,75,236,35,-1,6,-1],
                                                   [272,175,175,194,56,-1,-1,-1],
                                                    [109,161,93,222,58,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([58,'room58_level2_hallwayleft',[backbuttonrect+[56,-1,-1,-1],
                                               [208,92,205,405,60,-1,-1,-1],
                                                   [8,3,164,522,58,-1,1,-1], # ms khin's room
                                                   [417,186,93,238,56,-1,-1,-1],
                                                    [577,173,46,371,62,-1,1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([59,'room59_level2_mrballyntine',[backbuttonrect+[2,-1,-1,-1]]])
    roomslist.append(room)  


    room = Oofff.Room([60,'room60_level2_mslee_awake',[
                                               [403,207,215,141,61,-1,-1,-1],
                                                 [113,186,55,206,58,-1,-1,-1]]])
    roomslist.append(room)


    room = Oofff.Room([61,'room61_level2_mslee_board',[backbuttonrect+[60,-1,-1,-1]
                                               ]])
    roomslist.append(room)

    room = Oofff.Room([62,'room62_level2_mssusan',[backbuttonrect+[58,-1,-1,-1]
                                               ]])
    roomslist.append(room)


    room = Oofff.Room([63,'room63_level2_myanmarstudies',[backbuttonrect+[2,-1,-1,-1]
                                               ]])
    roomslist.append(room)

    room = Oofff.Room([64,'room64_level2_stairwell',[backbuttonrect+[56,-1,-1,-1],
                                                     [563,2,235,523,56,-1,-1,-1],
                                                     [0,462,88,131,79,-1,-1,-1],
                                                     [111,447,205,146,38,-1,-1,-1]
                                               ]])
    roomslist.append(room)

    room = Oofff.Room([65,'room65_level2_start',[backbuttonrect+[61,-1,-1,-1],
                                               [394,154,210,134,61,-1,-1,-1]]])
    roomslist.append(room)
    
    room = Oofff.Room([66,'room66_level3_conference_painting',[backbuttonrect+[67,-1,-1,-1]]])
    roomslist.append(room)
    
    room = Oofff.Room([67,'room67_level3_conference',[backbuttonrect+[68,-1,-1,-1],
                                               [708,137,64,52,66,-1,-1,-1]
                                               ]])
    roomslist.append(room)

    room = Oofff.Room([68,'room68_level3_hallway1',[backbuttonrect+[70,-1,-1,-1],
                                               [330,179,75,160,67,-1,1,-1],
                                               [1,154,32,259,75,-1,1,-1],
                                               [757,130,42,319,79,-1,-1,-1],
                                               [135,181,192,163,69,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([69,'room69_level3_hallway2',[backbuttonrect+[79,-1,-1,-1],
                                               [326,244,65,143,78,-1,1,-1],
                                               [728,192,72,270,75,-1,1,-1],
                                               [395,226,174,135,68,-1,-1,-1],
                                                [62,213,37,240,79,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([70,'room70_level3_hallwayright',[backbuttonrect+[69,-1,-1,-1],
                                               [315,48,114,198,69,-1,-1,-1],
                                               [462,150,41,188,78,-1,1,-1],
                                               [643,22,139,451,77,-1,1,-1]]])
    roomslist.append(room)


    room = Oofff.Room([71,'room71_level3_library_books',[backbuttonrect+[75,-1,-1,-1]
                                               ]])
    roomslist.append(room)

    room = Oofff.Room([72,'room72_level3_library_computerclose',[backbuttonrect+[73,-1,-1,-1]
                                              ]])
    roomslist.append(room)
    
    room = Oofff.Room([73,'room73_level3_library_computers',[backbuttonrect+[76,-1,-1,-1],
                                               [378,217,184,195,72,-1,-1,-1]
                                             ]])
    roomslist.append(room)
    
    
    room = Oofff.Room([74,'room74_level3_library_couches',[backbuttonrect+[76,-1,-1,-1]
                                            ]])
    roomslist.append(room)
    

    room = Oofff.Room([75,'room75_level3_library_entrance',[backbuttonrect+[68,-1,-1,-1],
                                               [208,225,524,236,76,-1,-1,-1],
                                               [710,219,90,248,71,-1,-1,-1]]])
    roomslist.append(room)

    room = Oofff.Room([76,'room76_level3_library',[backbuttonrect+[75,-1,-1,-1],
                                               [546,243,254,210,74,-1,-1,-1],
                                               [23,246,139,171,73,-1,-1,-1]
                                              ]])
    roomslist.append(room)

    room = Oofff.Room([77,'room77_level3_mrkelley',[backbuttonrect+[70,-1,-1,-1]]])
    roomslist.append(room)
    
    room = Oofff.Room([78,'room78_level3_mrroland',[backbuttonrect+[70,-1,-1,-1]
                                               ]])
    roomslist.append(room)

    room = Oofff.Room([79,'room79_level3_stairwell',[backbuttonrect+[68,-1,-1,-1],
                                               [551,1,249,559,68,-1,-1,-1],
                                               [115,453,255,133,64,-1,-1,-1]
                                              ]])
    roomslist.append(room)

    room = Oofff.Room([80,'room80_0_physics_drawer_key',[backbuttonrect+[26,-1,-1,-1],
                                                    [355,311,244,157,80,1,-1,3]]],
                      [80,'room80_1_physics_drawer_nokey',[backbuttonrect+[26,-1,-1,-1]
                                                       ]])
    roomslist.append(room)
    
    return roomslist
                                
                                            
    ## need 80-85
                      
