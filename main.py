
remember = {import:remember-plugin}
version = 0.7.8b
title
  Free unlimited Koto's Image Constructor Kit (KICK), don't type it, just click it.  
//Main
prompt // telling AI what we want to see, calling lists and join them
  $output = [this.selectAll]
  Defining //Defining the vars (after the reset or the first time)
    $output = [this.selectAll]
    [charNum=charNum||1, actor=actor||"Any actor", gender=gender||"♀️Female", age=age||18, bodyType=bodyType||"Any body type",""]
    [ethnicity=ethnicity||"Any ethnicity", aesthetic=aesthetic||"Any aesthetic",""]
    [eyeColor=eyeColor||"Any", eyeWear=eyeWear||"Any eyewear",""]
    [hairColor=hairColor||"Any", hairLength=hairLength||"Any length", hairStyle=hairStyle||"Any hairstyle", hairBody=hairBody||"Any body hair",""]
    [clothingTop=clothingTop||"Any clothes", clothingTopColor=clothingTopColor||"Any", clothingTopPattern=clothingTopPattern||"Plain", ""]
    [lingerieTop=lingerieTop||"Any top lingerie", lingerieTopColor=lingerieTopColor||"Any", lingerieTopPattern=lingerieTopPattern||"Plain", ""]
    [clothingBottom=clothingBottom||"Any bottom", clothingBottomColor=clothingBottomColor||"Any", clothingBottomPattern=clothingBottomPattern||"Plain",""]
    [lingerieBottom=lingerieBottom||"Any bottom lingerie", lingerieBottomColor=lingerieBottomColor||"Any", lingerieBottomPattern=lingerieBottomPattern||"Plain", ""]
    [legwear=legwear||"Any legwear", leing||"Any lighting", weather=weather||"Any weather", vibe=vibe||"Any vibe",""]
    [style=style||"Photo📷", filter=filter||"AgwearColor=legwearColor||"Any",""]
    [footwear=footwear||"Any footwear", footwearColor=footwearColor||"Any",""]
    [headwear=headwear||"Any headwear", headwearColor=headwearColor||"Any",""]
    [accessories=accessories||"Any accessories",""]
    [features=features||"Any", makeup=makeup||"Any makeup",""]
    [nails=nails||"Any", condition=condition||"Any condition",""]
    [pose=pose||"Any pose", view=view||"POV🎞", mood=mood||"Any expression",""]
    [holeType=holeType||1, thingType=thingType||1,""]
    [scene=scene||"Any scene", lighting=lightny filter",""]
    [imgNum=imgNum||2, resolution=resolution||"768x768", guidanceScale=guidanceScale||7,""]
  Declaration //Declaring the vars we're going to use in the lists
    $output = [this.selectAll]
    [fileName="{0-9}{a-z}{A-Z}".selectMany(10).join(""),""]
    [beVerb=[charNum==1?"is":"are"],""][haveVerb=[charNum==1?"has":"have"],""][plural=charNum==1?"":"s",""][position=""]
    [actorType=[/angel|demon|dryad|elf|fairy|furry|mermaid|minotaur|person|vampire/i.test(actor)?"humanoid":/bird|cat|dog|fox|horse|koala|monkey|mouse|panda|rabbit|unicorn|wolf/i.test(actor)?"animal":"other"],""]
    [actorReference=[actorList.gender[gender]].selectOne,""]
    [actorPreEvaluate=[actorType=="other"&&actor!="Any actor"?actorList.actor[actor].selectAll.filter(item => String(item).trim()!="").joinItems(", ").replace(/,+/g, ',').replace(/ ,/g, ',').replace(/\s{2,}/g, ' '):""],""]
    [tribal=[/ancient|prehistoric/i.test(vibe)?vibe.lowerCase:"{aztec|fula|inca|massai|maya|nuba|viking|zulu}".evaluateItem], ""]
    sceneType(type)=>
      switch(type){
        case "atmosphere": return /colorful|cosy|dramatic|dreamy|fresh|gloomy|horror|luxury|magical|messy|mysterious|party|romantic|simplistic|18/i.test(vibe);
        case "background": return /animals|crowd|people|fire|flowers|landscape|ufo|vehicles/i.test(vibe);
        case "cold": return sceneOpenAir&&(/ice|snow|tundra/i.test(scene)||/snow/i.test(weather)||/winter/i.test(vibe))||/cold/i.test(condition);
        case "dirty": return /apocalyptic|messy/i.test(vibe)||condition=="Dirty";
        case "drawnCurtains": return (/candle|lamp/i.test(lighting)||vibe=="Cosy"||/romantic|18/i.test(vibe))&&(/attic|bed|chair|couch|desk|fireplace|hotel|sofa|TV/i.test(scene)||scene=="Room");
        case "era": return /ancient|apocalyptic|cyberpunk|futuristic|medieval|prehistoric|renaissance|soviet|steampunk|wild west|50|80/i.test(vibe);
        case "explicit": return sceneSex||/flash|lap dance|touch/i.test(pose)||/abuse|came|deflor|strip/i.test(condition)||sceneNude||/18/i.test(vibe);
        case "handsFree": return /any pose|bending|bowing|crouching|kneeling|levitating|lying|on the|running|sitting|squatting|standing|turned around|walking/i.test(pose);
        case "hasRim": return  /balle|bath|bride|cheerleader|dress|flight|formal|gown|hanbok|high fasion|kimono|lolita|maid|nun|nurse|office|robe|secretary|stuardess|teacher|towel|waitress|whore/i.test(clothingTop)||/skirt/i.test(clothingBottom);
        case "highlights": return /Alien relic|Big Ben|Chernobyl|Chichen Itza|Christ the Redeemer|Colosseum|Eiffel Tower|Forbidden City|Great Wall of China|Hermitage|Kremlin|Leaning Tower of Pisa|Louvre|Lost city of Atlantis|Machu Picchu|Niagara Falls|Notre Damme de Paris|Pantheon|Persepolis|Petra|Pyramids|Red Square|Cathedral|Sphinx|Statue|Stonehenge|Sydney|Taj|Temple|Victoria|Washington|White House|Ziggurat/i.test(scene);
        case "horizontal": return /balcony|bed|bench|chair|couch|counter|desk|escalator|fountain|hammock|porch|sink|sofa|stage|stair|stool|stove|swing|table|toilet|seat|wash/i.test(scene)||scene=="Rock";
        case "hot": return /desert|hot|jungle|oasis|sand|sauna/i.test(scene)||scene == "Spa"||(sceneOpenAir&&/summer/i.test(vibe)&&/day/i.test(lighting))||condition=="Hot";
        case "location": return /backstage|bar|barn|cafe|club|dolphinarium|factory|farm|fasion|fireplace|fire station|gas station|gym|hawker stall|log fire|office|open air|opera|outdoor market|planetarium|restaurant|skyscraper|stable|supermarket|studio|trade center|TV screen|volcano|warehouse|waterfall|waterpark|zoo/i.test(scene);
        case "nude": return /no clothes/i.test(clothingTop);
        case "openAir": return /any scene|alley|balcony|beach|bench|boat|bridge|canyon|cave|cliff|court|cycle|desert|farm|fence|field|flowerbed|forest|fountain|garden|gas station|grass|grotto|hammock|hawker stall|haystack|hill|horse|hut|iceberg|ice maze|ice rink|jungle|lake|log fire|meadow|oasis|ocean|open air|outdoor|paraglider|park|playground|pond|porch|promenade|road|roof|sand|scooter|shore|sidewalk|snow|stadium|street|swings|tent|town square|train station|tundra|wall|wasteland|waterfall|wheat|yard|zoo/i.test(scene)||sceneHighlights||scene=="Rock"||scene=="River"||scene=="Counter";
        case "sex": return /job|oral|sex/i.test(pose);          
        case "seasons": return /autumn|christmas|spring|summer|winter/i.test(vibe);
        case "space": return /black hole|orbit|space/i.test(scene);
        case "surface": return /beach|bridge|carpet|cliff|cushion|floor|grass|hay|hill|iceberg|ice rink|laundry|meadow|ocean|parking|pillow|playground|promenade|road|roof|rug|sand|shore|sidewalk|snow|surface|towel|town square|treadmill|wheat|yoga mat/i.test(scene);
        case "suspendable": return /cliff|balcony|balloon|bridge|paraglider|pole/i.test(scene);
        case "transportation": return /airship|boat|bus|cruise|cycle|helicopter|horse|motorboat|plane|paraglide|scooter|steamer|tractor|tram|truck|yacht/i.test(scene)||scene=="Car"||scene=="Ship"||scene=="Train";
        case "underwater": return /fish tank|Jupiter|lost city|underwater/i.test(scene);
        case "vegetation": return vibe=="Flowers"||/field|forest|garden|greenhouse|jungle|meadow/i.test(scene)||scene=="Park";
        case "vertical": return /corner|door|fence|fish bowl|frige|mirror|pole|wall|wardrobe|window/i.test(scene);
        case "weightless": return sceneSpace||sceneUnderwater||/levitating/i.test(pose);
        case "wet": return /bathtub|beach|falls|fish tank|hot tub|jacuzzi|Jupiter|lake|ocean|pond|pool|shower|shore|Titan|water/i.test(scene)||sceneUnderwater||condition=="Wet"||(weather=="Rainy"&&accessories!="Umbrella"&&sceneOpenAir)||scene=="River"||scene=="Spa";
        case "windowless": return /backstage|basement|bathroom|boxing|closet|corner|club|dolphinarium|dungeon|escalator|fasion|garage|hot tub|jakuzzi|laboratory|laundry|lift|locker|opera|planetarium|photobooth|pole|sauna|stage|shower|submarine|subway|supermarket|theatre|toilet|warehouse|washing machine/i.test(scene)||scene=="Spa";
        default: false;
      }
    [sceneUnderwater=this.sceneType("underwater"), sceneSpace=this.sceneType("space"), sceneWeightless=this.sceneType("weightless"),""]
    [sceneHighlights=this.sceneType("highlights"), sceneOpenAir=this.sceneType("openAir"), sceneWindowless=this.sceneType("windowless"), sceneDrawnCurtains=this.sceneType("drawnCurtains"),""]
    [sceneCold=this.sceneType("cold"), sceneHot=this.sceneType("hot"), sceneDirty=this.sceneType("dirty"), sceneWet=this.sceneType("wet"),""]
    [sceneNude=this.sceneType("nude"), sceneSex=this.sceneType("sex"), sceneExplicit=this.sceneType("explicit"),""]
    [sceneVegetation=this.sceneType("vegetation"), sceneTransportation=this.sceneType("transportation"),""]
    [sceneHorizontal=this.sceneType("horizontal"), sceneVertical=this.sceneType("vertical"), sceneSurface=this.sceneType("surface"),""]
    [sceneLocation=this.sceneType("location"), sceneSuspendable=this.sceneType("suspendable"), sceneHandsFree=this.sceneType("handsFree"),""]
    [vibeSeasons=this.sceneType("seasons"), vibeEra=this.sceneType("era"), vibeBackground=this.sceneType("background"), vibeAtmosphere=this.sceneType("atmosphere"),""]
    [windowType=[vibe=="Prehistoric"||/cave|grotto/i.test(scene)?"cave entrance":/cage|jail/i.test(scene)?"bars":/tent/i.test(scene)?"unzipped tent entrance":vibe=="Post-apocalyptic"?"broken window":"{small ^3|medium |large |}window"],""]
    [clothingHasRim=this.sceneType("hasRim"),""]
    dimensions()=>
      let result="";
      if (/any scene|blank/i.test(scene)){return "";
      }else if (sceneSurface) {
        result+=" on the ";
        if (/surface/.test(scene)){result+="surface of ";}
      }else if (sceneHighlights) {result+=" at the ";
      }else if (sceneLocation) {result+=" at {a} ";
      }else if (sceneHorizontal) {result+=" on the edge of {a} ";
      }else if (sceneVertical) {result+=" against {a} ";
      }else if (sceneTransportation) {result+=" on the seat of {a} ";
      }else {result+=" in "+[scene=="Space"?"":"{a} "];}
      if (sceneHighlights){result+=scene;
      }else{result+=scene.lowerCase;}
      return result;
    [sceneDimensions=this.dimensions(),""]
    camera()=>
      let result=new Array(4).fill(""), angle=""
      if (/ears|eyes|head|face|lips|neck|portrait|shoulder|upper/i.test(view)){result[0]+="top";} //zoomed in on the head, neck
      if (/back|chest|hand|neck|portrait|stomach|upper/i.test(view)){result[1]+="mid";} //zoomed in on the neck, chest, stomach, hands
      if (/feet|glute|lower|thighs/i.test(view)){result[2]+="low";} //thighs, hips, knees, ankles, feet visible
      if (/bending sex|doggy|revers/i.test(pose)||/back|behind|glutes|shoulder|stalker/i.test(view)){result[3]+="rear";} //behind
      angle=result.selectAll.filter(item => String(item).trim()!="").joinItems("-");
      if(angle==""){angle="top-mid-low";} //everything is visible from the front/side but not the rear
      return angle;
    [camera=this.camera(),""][cameraAngles=camera.split("-"), /-rear/i.test(camera)?cameraAngles.shift():"",""]
    [POV=[camera=="top-mid-low"||/POV|stalker|voyeur/i.test(view)?"first person"+[/POV|stalker|voyeur/i.test(view)?" young man":""]:[gender=="♀️Female"?"male":"female"]],""][chest=[age>=18?"nipples":"chest"],""]
    [thing=[/female/i.test(POV)?"male's ":"[POV]'s "]+[thingType==4?"right hand middle finger":thingType==3?"dildo in hand":thingType==2?"strap-on":[age>=18?"penis":"male shaft"]],""]
    [holeRear=[gender=="♀️Female"?[age>=18?"anal hole":"rear hole"]:"bunghole"],""]
    [hole=/oral/i.test(pose)?"mouth":/fair/i.test(actor)?"arms and legs":pose=="Handjob"?"hand":/titjob/i.test(pose)&&age<18?"teats and hand":pose=="Titjob"?[age>=18?"tits":"chest"]:/merm/i.test(actor)?"mouth":pose=="Footjob"?"feet":holeType==1?[gender=="♀️Female"?[age>=18?"vaginal hole":"pudendal hole"]:"bunghole"]:holeRear,""]
    [holeReference=[/job|oral/i.test(pose)||/fair|merm/i.test(actor)?[age>=18?"vaginal hole":"privy hole"]:hole],""]
    covered()=>
      let result=[];
      if (/catwoman|ninja|pilot|spacesuit/i.test(clothingTop)||/burqa|hijab|motocycle/i.test(headwear)||/blindfold|sunglasses|VR/i.test(eyeWear)||/mask|muzzle/i.test(accessories)){result.push("top")};
      if ((!/bikini|bra|bustier|corset|dress|top/i.test(clothingTop))&&/angel|demon|fair/i.test(actor)){result.push("mid");result.push("rear");}
      return result;
    [covered=this.covered(),""]
  Main //The main lists
    $output = [this.selectAll.filter(paragraph => String(paragraph).trim()!="").joinItems(".\n")]
    Description
      $output = [this.selectAll.filter(line => String(line).trim()!="").joinItems(". ").sentenceCase]
      actor()=>
        if (actor=="Any actor"){return "";}
        let sentence=[];
        //actor
        if (/panorama|stalker/i.test(view)&&scene!="Any scene"){
          sentence.push("Long shot of "+[sceneHighlights?"the "+scene:"{a} "+scene.lowerCase]+[/balcony|hammock|parking lot|porch|roof|yard/i.test(scene)||!sceneOpenAir?" of a neighbouring {building|apartment} in the distance":" in the distance"]+" with ");
        }else if (camera!="rear"&&camera!="top-mid-low"){sentence.push("the view of "+view.lowerCase+[view.slice(-1)!="s"?plural:""]+" of ");
        }else {sentence.push("the "+[sceneExplicit?"intimate ":""]+"scene with ");}
        sentence.push([charNum==4?"a group of ":charNum==3?"three ":charNum==2?"a pair of ":"{a} "]);
        if (actorType=="humanoid"){
          //aesthetic first half
          if (aesthetic!="Any aesthetic"&&cameraAngles.includes("top")&&!covered.includes("top")){sentence.push(aesthetic.lowerCase+" ");}
          //ethnicity
          if (ethnicity!="Any ethnicity"&&actorType!="other"){sentence.push([actorList.ethnicity[ethnicity].getLength>0?actorList.ethnicity[ethnicity].joinItems(", "):ethnicity]+" ");}
          if (age!=0){
            sentence.push(age+" years old ");
            sentence.push([age>=70?"elderly ":age>=60?"senior ":age>=50?"middle-aged ":age>=40?"mature ":age>=35?"adult ":age>=20?"young ":age>=13?"teen ":age>=9?"preteen ":age>=6?"child ":age>=4?"little child ":age>=2?"baby ":"newborn baby "]);
          }
        }
        if (actorType!="other"){
          sentence.push(actorReference.subject);
          sentence.push(actorList.actor[actor].selectAll.filter(item => String(item).trim()!="").joinItems(", "));
        }else{sentence.push(actorPreEvaluate);}
        sentence.push(actorList.actor[actor].getPropertyKeys.map(property => cameraAngles.includes(property)&&(property!="top"||!covered.includes("top"))?actorList.actor[actor][property]:"").filter(item => String(item).trim()!="").join(", "));
        if (actorType=="humanoid"){
          //aesthetic second half
          if (aesthetic!="Any aesthetic"&&cameraAngles.includes("top")&&!covered.includes("top")){sentence.push(actorList.aesthetic[aesthetic].joinItems(", "));}
          //bodyType
          if (bodyType!="Any body type"){
            sentence.push(actorList.bodyType[bodyType].selectAll.filter((item,index) => `${index==0?'':item}`).joinItems(", "));
            sentence.push(actorList.bodyType[bodyType].getPropertyKeys.map(property => cameraAngles.includes(property)?actorList.bodyType[bodyType][property]:"").filter(item => String(item).trim()!="").join(", "));
          }
        }
        if (actorType=="humanoid"||actorType=="animal"){
          //eyes
          if (eyeColor!="Any"&&!/sleep/i.test(pose)&&mood!="Eyes closed"&&cameraAngles.includes("top")&&!covered.includes("top")){sentence.push(eyeColor.lowerCase+" eyes");}
          if (eyeWear!="Any eyewear"&&/top|rear/i.test(camera)&&camera!="low-rear"&&actorType=="humanoid"){
            if (/rear/i.test(camera)){sentence.push("the angle allows to see only the ");}
            if (eyeColor!="Any"&&covered.includes("top")){sentence.push(eyeColor.lowerCase+" ");}
            sentence.push(eyesList.eyeWear[eyeWear].getPropertyKeys.map(property => cameraAngles.includes(property)?eyesList.eyeWear[eyeWear][property]:"").filter(item => String(item).trim()!="").join(", "));
          }
          //hair
          if (hairLength=="Bald♂️"){sentence.push("completely bald");
          }else if ((sceneWeightless||sceneDirty||sceneWet||hairColor!="Any"||hairLength!="Any length"||hairStyle!="Any hairstyle")&&camera!="low"&&camera!="low-rear"){
            if ((camera=="mid"||camera=="rear-mid")&&actorType=="humanoid"){sentence.push("the frame only shows the endings of the ");}
            if (sceneWeightless){sentence.push("floating ");}
            if (sceneDirty){sentence.push("dirty ");}
            if (sceneWet||condition=="Wet hair"){sentence.push("wet ");}
            if (hairColor!="Any"){sentence.push(hairColor.lowerCase+" ");}
            if (hairLength!="Any length"){sentence.push(hairLength.lowerCase+" ");}
            if (hairStyle!="Any hairstyle"&&actorType=="humanoid"){
              sentence.push([hairList.hairStyle[hairStyle].getLength>1?hairList.hairStyle[hairStyle].selectAll.filter((item,index) => `${index==0?'': item}`).joinItems(", "):[actor=="🐦Bird"?"feathers":actorType=="animal"||actor=="😹Furry"?"fur":"hair"]+"with {a} "+hairStyle.lowerCase+" hairstyle"]);
            }
          }
          if (hairBody!="Any body hair"&&cameraAngles.some(angle=>hairList.hairBody[hairBody].getPropertyKeys.includes(angle))&&(!sceneExplicit||!/pube/i.test(hairBody))){
            sentence.push(hairList.hairBody[hairBody].getPropertyKeys.map(property => cameraAngles.includes(property)?hairList.hairBody[hairBody][property]:""));
          }
        }
        return combine(sentence);
      [this.actor()]
      clothes() =>
        let sentence=[], addedEffects=[];
        if (actorType=="animal"&&/🐾/i.test(accessories)){sentence.push(clothingList.Accessories[accessories].getPropertyKeys.map(property => cameraAngles.includes(property)?clothingList.Accessories[accessories][property]:"").filter(item => String(item).trim()!="").join(", "));}
        if (clothingTop=="Any clothes"||actorType!="humanoid"){return combine(sentence);}
        if (clothingTop=="No clothes"){return "completely stripped of any clothing";}
        let clothingFull=!/blouse|bra|bustier|camisole|corset|dress|fur coat|hoodie|jacket|pullover|shirt|sweater|top|turtleneck/i.test(clothingTop);
        let clothingUniform=/bride|cowboy|doctor|firefighter|formal|gothic|hanbok|judge|lolita|man|maid|martial|medieval armor|military|ninja|nun|pilot|pirate|police|prehistoric|sailor|samurai|santa|scuba|spacesuit|witch|woman/i.test(clothingTop);
        let showLingerieTop=/blouse|dress|top/i.test(clothingTop)&&!clothingFull;
        let showLingerieBottom=(/balle|bath|bride|cheerleader|dress|flight|formal|gown|hanbok|high fasion|kimono|lolita|maid|nun|nurse|office|robe|secretary|stuardess|teacher|towel|waitress|whore/i.test(clothingTop)||/bottom|skirt/i.test(clothingBottom))&&!/pantyhose|tights/i.test(legwear)&&!clothingFull;
        let showLegwear=/bikini|any bottom|no bottom|boxers|briefs|pantes|short|skirt|string|thong|trunks/i.test(clothingBottom);
        let clothingThin=/balle|blouse|bra|bride|bustier|camisole|cheerleader|dress|formal|gymnast|lolita|maid|nightwear|nurse|school|shirt|teacher|top|whore/i.test(clothingTop);
        if (!clothingFull){
          //headwear
          if (headwear!="Any headwear"&&(/top/i.test(camera)||camera=="rear")){
            if (headwear=="No headwear"){
              sentence.push("no headwear");
            }else{
              if (sceneDirty){sentence.push("dirty ");}
              if (sceneWet){sentence.push("wet ");}
              if (headwearColor!="Any"){sentence.push(headwearColor.lowerCase+" ");}
              sentence.push(clothingList.Headwear[headwear].getLength>1?clothingList.Headwear[headwear].selectAll.filter((item,index) => `${index==0?'':item}`).joinItems(", "):headwear.lowerCase);
            }
          }
          //accessories
          if (accessories!="Any accessories"){
            sentence.push(clothingList.Accessories[accessories].getPropertyKeys.map(property => cameraAngles.includes(property)?clothingList.Accessories[accessories][property]:"").filter(item => String(item).trim()!="").join(", "));
            if (sceneWeightless){sentence.push("floating accessories");}
          }
        }
        //top
        if (clothingTop!="Any top"&&(cameraAngles.some(angle=>clothingList.Top[clothingTop].getPropertyKeys.includes(angle))||clothingTop=="No top")){
          if (clothingTop=="No top"){sentence.push("stripped of top clothing");
          }else{
            if (sceneDirty){sentence.push("dirty ");}
            if (sceneWet){
              sentence.push("wet ");
              if (clothingThin){sentence.push("sticking to the skin ");}
            }
            if (!clothingUniform){
              if (clothingTopColor!="Any"){sentence.push(clothingTopColor.lowerCase+" ");}
              if (clothingTopPattern!="Any"){sentence.push(clothingTopPattern.lowerCase+" ");}
            }
            sentence.push(clothingList.Top[clothingTop].getPropertyKeys.map(property => cameraAngles.includes(property)&&(!/merm|minotaur/i.test(actor)||property!="low")?clothingList.Top[clothingTop][property]:"").filter(item => String(item).trim()!="").join(", "));
            if (sceneExplicit&&!/rear/i.test(camera)){
              if (clothingFull){sentence.push("the top part is ");}
              if (/t-shirt/i.test(clothingTop)){
                sentence.push("pulled up to the neck");
              }else if (/coat|cowgirl|doctor|flight|formal|jacket|leather|lolita|maid|office|outerwear|police|school|secretary|shirt|stuardess|teacher|waitress|whore/i.test(clothingTop)){
                sentence.push("unbuttoned and pulled aside");
              }else if (/blouse|bride|goth|fasion|night|swimsuit|wonderwoman/i.test(clothingTop)){
                sentence.push("pulled down on the neckline");
              }else if (/bra/i.test(clothingTop)){
                sentence.push("unfastened and pulled aside");
              }else if (/armor|balle|geisha|hanbok|kimono|kisen|martial|prehistoric|towel|witch|yukata/i.test(clothingTop)){
                sentence.push("unlaced and pulled aside");
              }else if (/bodysuit|catwoman|latex|pilot|scuba|tracksuit/i.test(clothingTop)){
                sentence.push("unzipped and pulled aside");
              }else if(/dress|santa/i.test(clothingTop)){
                sentence.push("pulled down on the neckline");
              }else if(/gymnast/i.test(clothingTop)){
                sentence.push("ripped in half and pulled aside");
              }else{
                sentence.push("pulled up to the neck"); 
              }
              sentence.push("exposing the [chest]");
              if ((clothingFull||/dress/i.test(clothingTop))&&!/handjob|oral/i.test(pose)&&!/merm/i.test(actor)&&camera!="top"&&camera!="mid"){
                sentence.push("and on the lower part ");
                if (/construct|cowgirl|leather|military|ninja|outerwear|pilot|police/i.test(clothingTop)){
                  sentence.push("unbuttoned and pulled down");
                }else if (/bodysuit|catwoman|coat|hanbok|kimono|kisen|slave|swimsuit|yukata/i.test(clothingTop)){
                  sentence.push("pulled aside");
                }else if (/gymnast/i.test(clothingTop)){
                  sentence.push("ripped in half in the middle forming a hole and");
                }else if (/armor|casual|latex|prehistoric|santa|scuba|spacesuit|sports|tracksuit|wonderwoman/i.test(clothingTop)){
                  sentence.push("stripped down");
                }else{sentence.push("pulled up high by the rim");}
                if (clothingFull){sentence.push("exposing the [holeReference]");}
              }
            }else{
              if (/day|sun/i.test(lighting)&&/any weather|clear/i.test(weather)&&clothingThin){addedEffects.push("the sunlight accentuates the [actorReference.subject]'s silhouette"+[!/any top|no top/i.test(lingerieTop)?" and makes [lingerieTop.lowerCase] slightly visible":""]+" through the thin clothing, outlining the [actorReference.subject]'s figure");}
            }
            if (sceneWeightless){addedEffects.push("floating clothing");}  
          }
        }
        //lingerie top
        if (showLingerieTop&&lingerieTop!=="Any top lingerie"&&cameraAngles.some(angle=>clothingList.lingerieTop[lingerieTop].getPropertyKeys.includes(angle))){
          if (lingerieTop=="No top lingerie"){sentence.push("no bra");
          }else{
            if (clothingTop!=="Any top"&&clothingTop!=="No top"&&!sceneExplicit){
              if (vibe=="Romantic"||/massage|kissing|sleep/i.test(pose)||sceneHot){sentence.push("the top clothing is loose showing much of the ");
              }else{sentence.push("under the [clothingTop.lowerCase], there are partially visible straps of the ");}
            }else{
              if (lingerieTopColor!=="Any"){sentence.push(lingerieTopColor.lowerCase+" ");}
              if (lingerieTopPattern!=="Any"){sentence.push(lingerieTopPattern.lowerCase+" ");}
            }
            sentence.push(clothingList.lingerieTop[lingerieTop].getPropertyKeys.map(property => cameraAngles.includes(property)&&(!/merm|minotaur/i.test(actor)||property!="low")?clothingList.lingerieTop[lingerieTop][property]:"").filter(item => String(item).trim()!="").join(", "));
          }
        }
        if (clothingFull||/merm/i.test(actor)||camera=="top"){
          let result=combine(sentence), effects=combine(addedEffects);
          return [result!=""?"the [actorReference.subject] [beVerb] wearing {a} "+result+[effects!==""?", "+effects:""]:result];
        }
        //bottom
        if (clothingBottom!="Any bottom"){
          if (clothingBottom=="No bottom"){
            sentence.push([clothingTop=="No top"?"completely stripped of any":"stripped of bottom"]+" clothing");
          }else{
            if (sceneDirty){sentence.push("dirty ");}
            if (sceneWet){sentence.push("wet ");}
            if (clothingBottomColor!="Any"){sentence.push(clothingBottomColor.lowerCase+" ");}
            if (clothingBottomPattern!="Any"){sentence.push(clothingBottomPattern.lowerCase+" ");}
            sentence.push(clothingList.Bottom[clothingBottom].getLength>1?clothingList.Bottom[clothingBottom].selectAll.filter((item,index) => `${index == 0 ? '': item}`).joinItems(", "):clothingBottom.lowerCase);
            if (sceneExplicit&&!/handjob|oral/i.test(pose)&&camera!="top"){
              if (/skirt/i.test(clothingBottom)){
                sentence.push("pulled up high by the rim");
              }else if (/leggings|tights|yoga/i.test(clothingBottom)){
                sentence.push("ripped in half in the middle forming a hole and");
              }else if (/denim|jeans|pants|shorts|trousers/i.test(clothingBottom)){
                sentence.push("unbuttoned and pulled down");
              }else{
                sentence.push("pulled down");
              }
              sentence.push("exposing the [holeReference]");
            }
          }
        }
        //lingerie bottom
        if (showLingerieBottom&&lingerieBottom!=="Any bottom lingerie"&&camera!="top"&&camera!=="mid"){
          if (lingerieBottom=="No bottom lingerie"){sentence.push("no "+[age>=18?"":"under"]+"panties");
          }else{
            if (lingerieBottomColor!=="Any"){sentence.push(lingerieBottomColor.lowerCase+" ");}
            if (lingerieBottomPattern!=="Any"){sentence.push(lingerieBottomPattern.lowerCase+" ");}
            sentence.push(clothingList.lingerieBottom[lingerieBottom].getLength>1?clothingList.lingerieBottom[lingerieBottom].selectAll.filter((item,index) => `${index==0?'':item}`).join(", "):lingerieBottom.lowerCase);
            if (sceneExplicit&&!/handjob|oral/i.test(pose)&&camera!="top"){
              if (/panties|strings|thong/i.test(lingerieBottom)){sentence.push("pulled aside");
              }else {sentence.push("pulled down");}
              sentence.push("exposing the [holeReference]");
            }
          }
        }
        //legwear
        if (legwear!="Any legwear"&&showLegwear&&camera!="top"&&camera!="mid"){
          if (legwear == "No legwear"){
            sentence.push("no legwear");  
          }else{
            if (sceneDirty){sentence.push("dirty ");}
            if (sceneWet){sentence.push("wet ");}
            if (legwearColor!="Any"){sentence.push(legwearColor.lowerCase+" ");}
            sentence.push(clothingList.Legwear[legwear].getLength>1?clothingList.Legwear[legwear].selectAll.filter((item,index) => `${index == 0 ? '': item}`).joinItems(", "):legwear.lowerCase);
          }
        }
        //footwear
        if (footwear!="Any footwear"&&(camera=="rear"||/low/i.test(camera))){
          if (footwear=="No footwear"){
            sentence.push("barefoot");
          }else{
            if (sceneDirty){sentence.push("dirty ");}
            if (sceneWet){sentence.push("wet ");}
            if (footwearColor!="Any"){sentence.push(footwearColor.lowerCase+" ");}
            sentence.push(clothingList.Footwear[footwear].getLength>1?clothingList.Footwear[footwear].selectAll.filter((item,index) => `${index == 0 ? '': item}`).joinItems(", "):footwear.lowerCase);
          }
        }
        let result=combine(sentence), effects=combine(addedEffects);
        return [result!=""?"the [actorReference.subject] [beVerb] wearing {a} "+result+[effects!==""?", "+effects:""]:result];
      [this.clothes()]
      features() =>
        let sentence=[];
        if (actor=="Any actor"){return "";}
        if (sceneDirty||sceneWet){
          if (sceneDirty){sentence.push("dirty ");}
          if (sceneWet){sentence.push("wet ");}
          if (actor=="🐦Bird"){sentence.push("feathers");
          }else if (actor=="😹Furry"||actorType=="animal"){sentence.push("fur");
          }else if (actorType=="humanoid"){sentence.push("skin");
          }else if (actorType=="mechanical"){
            sentence.push("electronics");
            if (sceneWet){sentence.push("electric shortcuts, sparks fly, water vaporizes");}
          }
        }
        if (actorType!="humanoid"){return sentence.selectAll.filter(item => String(item).trim()!="").map((item,index,array) => String(item).slice(-1)==" "||index==array.length-1?item:item+", ").join("");}
        //features
        if (!/Any|No/.test(features)&&(!/brown|pink/i.test(features)||sceneExplicit)){
          let featuresProperty=featuresList.features[features];
          sentence.push(featuresProperty.selectAll.filter((item,index) => `${index==0?'': item}`).joinItems(", "));
          sentence.push(featuresProperty.getPropertyKeys.map(property => cameraAngles.includes(property)&&!covered.some(bodyPart => bodyPart==property)?featuresProperty[property]:"").filter(item => String(item).trim()!="").join(", "));
        }
        //makeup
        if (!/any makeup|no makeup/i.test(makeup)&&cameraAngles.includes("top")&&!covered.includes("top")){
          if (!/dry|tribal/i.test(makeup)){sentence.push(makeup.lowerCase+[/fake|contour|lipstick|no makeup/i.test(makeup)?"":" makeup"]);}
          sentence.push(featuresList.makeup[makeup].selectAll.filter((item,index) => `${index==0?'': item}`).joinItems(", "));
        }
        //nails
        let gloves=/armor|batman|body suit|catwoman|construction|detective|firefighter|goth|latex|leather suit|lolit|manda|martial|mittens|ninja|outerwear|pilot|sailor|santa|spacesuit|spiderman/i.test(clothingTop)||accessories=="Gloves";
        if (!nails=="Any"&&!/rear|top/i.test(camera)&&!gloves){
          if (sceneDirty){sentence.push("dirty ");}
          sentence.push(nails.lowerCase+" nail polish");
        }
        //condition
        if (!/condition|wet|dirty/i.test(condition)){
          sentence.push([featuresList.condition[condition].getLength>1?featuresList.condition[condition].selectAll.filter((item,index) => `${index==0?'': item}`).joinItems(", "):condition.lowerCase]);
        }
        if (sceneCold&&condition!="Cold"){
          sentence.push("very cold, shivering");
          if (cameraAngles.includes("top")){sentence.push("flushed nose and cheeks from cold temperatures");}
        }else if (sceneHot&&condition!="Hot") {sentence.push("{sweating, |}skin flushed from high temperatures");}
        return combine(sentence);
      [this.features()]
    Composition
      $output = [this.selectAll.filter(line => String(line).trim()!="").joinItems(". ").sentenceCase]
      pose() =>
        if (actor=="Any actor"){return "";}
        let sentence=[];
        if (pose!="Any pose"){
          if (sceneSex){
            if (actorType=="humanoid"&&POV=="man"){sentence.push("There is a partially visible [POV] next to the [actorReference.subject]");}
            if (charNum>=2){sentence.push("one of ");}
          }
          sentence.push("the ");
          if (pose!="Sex"){sentence.push(actorReference.subject+[sceneSex?" is ":" [beVerb] "]);}
          if (sceneWeightless){
            sentence.push("weightless and floating"+sceneDimensions);
            if (actorType=="humanoid"&&(sceneUnderwater&&!/scuba|spacesuit/i.test(clothingTop)&&!/merm/i.test(actor))||(sceneSpace&&!/rocket|station|spaceship/i.test(scene))){
              sentence.push("[actorReference.subject] [beVerb] gasping for air");
            }
          }else if (/merm/i.test(actor)&&sceneSex&&!/oral|handjob|titjob/i.test(pose)){
            sentence.push("lying[sceneDimensions] in front of the [POV] and having oral sex with them");
          }else if (/fair/i.test(actor)&&sceneSex){
            if (/oral/i.test(pose)){
              sentence.push("the [thing] is upright as tall as the [actorReference.subject], the [actorReference.subject] is climbing the [thing] to the tip and putting the tip in the mouth");
            }else{sentence.push("lying[sceneDimensions], the [thing] is covering the [actorReference.subject]'s entire body like a blanket, pressing [actorReference.pronounPossessive] down, the tip of the [thing] is over the [actorReference.subject]'s mouth. the [actorReference.subject] is embracing the [thing] from underneath with legs and arms");}
          }else{
            sentence.push([poseList.pose[pose].getLength>1?poseList.pose[pose].selectAll.filter(item => String(item).trim()!="").filter((item,index) => `${index==0?'':item}`).joinItems(", "):pose.lowerCase]);
            if (actorType=="humanoid"&&sceneSex&&pose!="Sex"&&(camera!="top"||!/oral/i.test(pose))){
              sentence.push(poseList.pose["Sex"].selectAll.filter(item => String(item).trim()!="").filter((item,index) => `${index==0?'':item}`).joinItems(", "));
            }
          }
        }
        return combine(sentence);
      mood()=>
        if (actor=="Any actor"){return "";}
        let sentence=[];
        if (mood!="Any expression"&&actorType=="humanoid"&&!/sleep/i.test(pose)&&cameraAngles.includes("top")&&!covered.includes("top")){
          sentence.push([poseList.mood[mood].getLength>1?poseList.mood[mood].selectAll.filter(item => String(item).trim()!="").filter((item,index) => `${index==0?'':item}`).joinItems(", "):mood.lowerCase]+" facial expression");
        }
        return combine(sentence);
      view()=>
        let sentence=[];
        if (view!="Any view"){sentence.push(poseList.view[view].selectAll.filter(item => String(item).trim()!="").filter((item,index) => `${index==0?'':item}`).joinItems(", "));}
        return combine(sentence);
      [this.pose()]
      [this.mood()]
      [this.view()]
      scene() =>
        let sentence=[];
        //scene
        if (scene=="Blank"){return "blank background";}
        if (scene!="Any scene"){
          if (actor=="Any actor"){
            sentence.push([sceneHighlights?scene:scene.lowerCase]);
            if (ethnicity!="Any ethnicity"&&!sceneHighlights&&!sceneWindowless&&!sceneVegetation&&!sceneSpace&&!/surface/i.test(scene)){sentence.push(" somewhere in a "+ethnicity+" "+[/futur|punk|urban/i.test(vibe)?"city":/small town|soviet|50/i.test(vibe)?"town":/animal|rural/i.test(vibe)?"village":"{city|{small |}town|village}"]);}
          }
          if (camera=="top-mid-low"||camera=="rear"){sentence.push(sceneList.scene[scene].selectAll.filter((item,index) => `${index==0?'':item}`).joinItems(", "));}
        }
        if (sceneDrawnCurtains){sentence.push("drawn curtains");}
        if (sceneUnderwater&&!/Jupiter/i.test(scene)){sentence.push("{school{s|} of fish|}".evaluateItem);}
        if (sceneWeightless){sentence.push("floating "+[sceneWet?"bubbles":/coffee|glass/i.test(accessories)?"beverage drops":/sweat/i.test(condition)?"sweat droplets":/leash|whip/i.test(accessories)?"tether":/messy|post-apocalyptic/i.test(vibe)?"garbage pieces and crums":"dust particles"]);}
        if (sceneWeightless||/surface/.test(scene)){return sentence.selectAll.filter(item => String(item).trim()!="").map((item,index,array) => String(item).slice(-1)==" "||index==array.length-1?item:item+", ").join("");}
        return combine(sentence);
      setting() =>
        if (scene=="Blank"||sceneWeightless||/surface/i.test(scene)){return "";}
        let sentence=[], outsideEvent=[];
        //vibe
        if (vibe!="Any vibe"){
          if (vibeSeasons&&!sceneOpenAir&&!sceneWindowless&&!sceneDrawnCurtains){outsideEvent.push(vibe.lowerCase);
          }else if (vibeEra){sentence.push(vibe+" era vibe");
          }else if (vibeAtmosphere){sentence.push(vibe.lowerCase+" atmosphere");}
          if(vibeAtmosphere||((vibeBackground||vibeSeasons||vibeEra)&&!sceneWindowless&&!sceneDrawnCurtains&&(camera=="top-mid-low"||camera=="rear"))){
            sentence.push(sceneList.vibe[vibe].selectAll.filter(item => String(item).trim()!="").filter((item,index) => `${index==0?'':item}`).joinItems(", "));
          }
          if(sceneOpenAir&&style!="Icon🖼"&&camera=="top-mid-low"){
            if (/town|urban/i.test(vibe)||/alley|balcony|parking|playground|roof|sidewalk|square|street/i.test(scene)){
              sentence.push("{|{a couple of |}pigeons {flying around|sitting on the {roof|road}}|}".evaluateItem);  
            }else{sentence.push("{bird{s|} in the sky|}".evaluateItem);}
            if (!sceneCold){sentence.push("{insects buzzing around|}".evaluateItem);}
          }
        }
        //weather
        if (weather!="Any weather"&&!sceneWindowless&&!sceneDrawnCurtains){
          if (!sceneOpenAir&&weather!="Breeze"){outsideEvent.push(weather.lowerCase);}
          if (camera=="top-mid-low"||camera=="rear"){sentence.push(sceneList.weather[weather].selectAll.filter(item => String(item).trim()!="").filter((item,index) => `${index==0?'':item}`).joinItems(", "));}
          if (sceneHot&&/hot tub|sauna|spa/i.test(scene)){sentence.push("steam in the air");}
        }
        //lighting
        let airPhenomenon=/aurora|fireworks|lightning|day|night|eclipse|sun|twilight/i.test(lighting);
        if (lighting!="Any lighting"){
          if (/bright|studio|spotlight/i.test(lighting)){sentence.push("edge lighting, low-contrast");}
          if (airPhenomenon&&!sceneWindowless&&!sceneOpenAir&&!sceneDrawnCurtains){outsideEvent.push(lighting.lowerCase);}
          if ((airPhenomenon&&!sceneWindowless&&!sceneDrawnCurtains&&(camera=="top-mid-low"||camera=="rear"))||!airPhenomenon){
            sentence.push(sceneList.lighting[lighting].selectAll.filter(item => String(item).trim()!="").filter((item,index) => `${index==0?'':item}`).joinItems(", "));
          }
        }
        if (outsideEvent.selectAll.filter(item => String(item).trim!="").join("")!=""&&!airPhenomenon&&weather!="Any weather"){outsideEvent.push("weather");}
        let result=combine(sentence), outside=outsideEvent.selectAll.filter(line => String(line).trim()!="").joinItems(" ");
        result=[outside==""?"":outside+" outside seen through the "+windowType]+[outside!=""&&result!=""?". ":""]+[result==""?"":result];
        return result;
      [this.scene()]
      [this.setting()]
    [userPrompt]
    Style and quality
      styleAndQuality()=>
        let sentence=[], qprefix=quality.split(" ")[0];
        sentence.push(qprefix+" high resolution");
        if (filter=="Any filter"){sentence.push(qprefix+" high quality");}
        sentence.push(qprefix+" sharp ");
        if (style!="Any style"){sentence.push(styleList.style[style].prompt.selectAll.filter(item => String(item).trim()!="").joinItems(", "));}
        if (filter!="Any filter"){
          sentence.push("using [filter] filter");
          sentence.push(styleList.filter[filter].selectAll.filter(item => String(item).trim()!="").joinItems(", "));
        }
        if (!/aperture/i.test(filter)&&!/stalker/i.test(view)&&camera=="top-mid-low"){sentence.push("infinite depth-of-field, with the entire image in focus");}
        if (actorType=="humanoid"){
          if (view=="Ears"){sentence.push("[details] ear skin and ear anatomy");
          }else if (view=="Eyes"){sentence.push("[details] skin around eyes, lifelike eyes");
          }else if (view=="Feet"||/foot/i.test(pose)){sentence.push("[details] foot skin");
          }else if (view=="Hands"){sentence.push("[details] hand skin");
          }else if (view=="Lips"){sentence.push("[details] lip skin");
          }else if (view=="Neck"){sentence.push("[details] neck skin");}
        }else if (actorType=="mechanical"){sentence.push("[quality] metal textures and reflections, [details] metal");}
        if (!/any scene|blank/i.test(scene)&&(camera=="top-mid-low"||camera=="rear")){sentence.push("[details] background");}
        return combine(sentence);
      $output = [this.styleAndQuality().sentenceCase]
    Settings
      $output = [this.selectAll.filter(line => String(line).trim() != "").joinItems("")]
      (negativePrompt:::[negativePrompt])
      (resolution:::[resolution])
      (width:::[width=resolution.replace(/x(\d+)/,"")])
      (height:::[height=resolution.replace(/(\d+)x/,"")])
      (guidanceScale:::[guidanceScale])
      (saveDescription:::[actor=="Any actor"?"":"{A} "+actorReference.subject][pose=="Any pose"?"":" "+pose.lowerCase][view=="Any view"?"":" from {a} "+view.lowerCase+" view"])
      (saveTitle:::[fileName])
 //<=Prompt
negativePrompt // removing items from the images
  $output = [this.selectAll.filter(item => String(item).trim() != "").joinItems(".\n").sentenceCase]
  [userNegativePrompt]
  negativeDescription()=>
    let sentence=[];
    if (actorType=="humanoid"){
      if (!/closed|drunk|mad/i.test(mood)&&!/sleep/i.test(pose)&&cameraAngles.includes("top")&&!covered.includes("top")){sentence.push("unfocused eyes");}
      if (gender=="♀️Female"&&!/heavy|lip/i.test(makeup)&&cameraAngles.includes("top")){sentence.push("enlarged lips, big lips, big mouth");}
      if (bodyType!="Any body type"){
        if (bodyType=="Petite"){
          sentence.push("fat, muscles, wide hips");
          if (sceneExplicit){sentence.push([/rear/i.test(camera)?"wide glutes, big glutes":"areolas"]);}
        }else if (/chubby|overweight/i.test(bodyType)){sentence.push("petite, fit, slim");}
      }
      if (sceneExplicit&&age<13){sentence.push("reached puberty, pubic hair, the [hole] is not based on age");}
      if (features=="No features"){
        sentence.push("tan");
        if (!/rear/i.test(camera)){sentence.push("blemishes, freckles, piercing");}
        if (camera!="top"){sentence.push("tattoo");}
      }
      if (makeup=="No makeup"&&!/rear/i.test(camera)){sentence.push("makeup, permanent makeup");}
      if (charNum>=2&&!/rear/i.test(camera)){sentence.push("twins, same faces");}
      if (hairBody=="No body hair"&&!/rear/i.test(camera)){
        sentence.push("facial hair, body hair");
        if (sceneExplicit){sentence.push("pubic hair");}
      }
    }
    return combine(sentence);
  [this.negativeDescription()]
  negativeComposition()=>
    let sentence=[];
    if (actor!="Any actor"&&view!="Any view"&&!/panorama|stalker/i.test(view)){
      sentence.push([camera=="top-mid-low"||camera=="rear"||actorType!="humanoid"?"the [actorReference.subject] [beVerb] ":"the "+view.lowerCase+[view.slice(-1)=="s"?" are ":" is "]]+"out-of-frame, cropped, not centered");
    }
    if (actorType=="humanoid"){
      sentence.push("mutation, extra limbs, unfinished, fused limbs, fused body parts");
      if (/oral/i.test(pose)){sentence.push("mutated mouth, mutated tongue");}
      if (sceneSex){sentence.push("mutated [thing], extra [thing]");}
    }
    if (!sceneOpenAir&&!sceneWindowless&&/rainy|snowy/i.test(weather)){sentence.push("weather effects at the foreground");}
    if (sceneSpace||/surface/.test(scene)){sentence.push("blue sky, water, vegetation, trees, atmosphere");}
    sentence.push(userNegativePrompt);
    return combine(sentence);
  [this.negativeComposition()]
  negativeStyle()=>
    const sentence=[];
    if (style!="Any style"){sentence.push("The style is "+styleList.style[style].negative.selectAll.filter(item => String(item).trim() != "").joinItems(", "));}
    if (filter=="Any filter"&&!/dreamy|dramatic|gloomy|horror|post-apocalyptic|prehistoric/i.test(vibe)){sentence.push("the image is black and white, desaturated"+[!/stalker/i.test(view)?", blurry":""]);}
    sentence.push("with copyright, text, watermark");
    let result=combine(sentence);
    return result+[result!=""?".":""];
  [this.negativeStyle()]
 //<=NegativePrompt
output // creating the object to use in the html code
  [image(prompt)]
 //<=Main
//Lists, the bulk of content
actorList // actor, gender, body type, ethnicity, aesthetic
  actor 
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="actor=this.value; updateDetailsVisibility(); updateClothingVisibility(); updateDropdowns();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="actor" ${item.getName==actor?'checked':item.getName=='<h3><b>humanoid</b></h3>'||item.getName=='<h3><b>animal</b></h3>'||item.getName=='<h3><b>other</b></h3>'||item.getName=='<h3><b>saved</b></h3>'?'disabled':''} /><label>${item.getName}</label></div>`).join('')]
    Any actor
    <h3><b>humanoid</b></h3>
    🧑Person
    👼Angel
      white glowing skin, slender
      light aura around the outline
      light particles and light bird feathers floating around
      top=angel halo above the head[hairColor=="Any"?", white hair":""]
      mid=wide span white bird wings
      rear=[camera=="low-rear"?"":this.top][camera!="low-rear"?", wide span white bird wings coming out of the shoulder blades":""]
    👿Demon
      demonic {charcoal black|red and black|red} skin, dark particles floating around
      top=short horns, sharp teeth, glowing eyes
      mid=wide span bat wings
      low=tail with a sharp tip, cloven feet
      rear=[camera=="low-rear"?"":this.top][camera!="low-rear"?", wide span bat wing coming out of the shoulder blades":""], [this.low]
    🌳Dryad
      slender, tree bark colored skin partially covered with leaves
      [camera!="low"&&camera!="low-rear"?"antlers":""]
      top=pointy ears, leaves and flowers and berries growing out of the hair[hairColor=="Any"?", green hair":""][/rear/i.test(camera)?"":", delicate features"]
      rear=[camera=="low-rear"?"":this.top]
    🧝‍♀️Elf
      glowing white skin
      top=pointy elf ears, delicate features[hairColor=="Any"?", white hair":""]
      mid=slender
      rear=[camera=="low-rear"?"":this.top], [this.mid]
    🧚‍♀️Fairy
      scaled down to 30 cm tall
      mid=wide span fairy wings, magical glow around the wings
      rear=[camera!="low-rear"?"wide span fairy wings coming out of the shoulder blades":""]
    😹Furry
      anthropomorphic animal[plural]
      top=animal ears
      low=animal tail, animal paws
      rear=[camera=="low-rear"?"":this.top][camera=="mid-rear"?"":", [this.low]"]
    🧜‍♀️Mermaid
      slender
      fish scales for skin
      [!sceneWet&&sceneOpenAir&&lighting=="Day"&&weather!="Rainy"?"suffering from dehydration":""]
      top=fins for ears, fin crest on the head, delicate features[hairColor=="Any"?", blue hair":""]
      mid=human upper body
      low=fish tail for legs bottom
      rear=[camera=="low-rear"?"":this.top], [this.mid][camera=="mid-rear"?"":", [this.low]"]
    🐂Minotaur
      bull fur
      extra muscular
      [camera!="low"&&camera!="low-rear"?"bull horns":""]
      top=bull head
      low=bull legs, bull hooves, bull tail
      rear=[camera=="low-rear"?"":this.top][camera=="mid-rear"?"":", [this.low]"]
    🧛‍♀️Vampire
      extremely pale skin devoid of blood
      [lighting=="Day"&&sceneOpenAir&&weather=="Clear"?"skin burning on contact with the sun causing agony, smoke rises from the skin":""]
      top=vampire fangs, delicate features, pale lips, dark circles under the eyes[eyeColor=="Any"&&mood!="Eyes closed"?", red irises":""]
      mid=[clothingTop=="Any"&&camera!="top"?"wearing vampire cape":""]
      rear=[camera=="low-rear"?"":this.top][clothingTop=="Any"&&camera!="top"?", wearing vampire cape":""]
    <h3><b>animal</b></h3>
    🐻Bear
    🐦Bird
    🐱Cat
    🐶Dog
    🐲Dragon
    🦊Fox
    🐴Horse
    🐨Koala
    🐒Monkey
    🐭Mouse
    🐼Panda
    🐇Rabbit
    🦄Unicorn
    🐺Wolf
    <h3><b>other</b></h3>
    👽Alien
      alien sentient being[plural]
      [alienType="{basalt|crystal|gaseous|humanoid|insect hive|jellyfish|ooze|metal|plantlife|robotic|silicon|stone|wooden|worm-like}".evaluateItem,""]
      [/metal|robotic|stone/i.test(alienType)?actorType="mechanical":/humanoid|silicon/i.test(alienType)?actorType="humanoid":actorType="other",""]
      unusual {blue|green|red|white|black|human|reptile|animal|furry|scaled|covered with feathers|transparent} skin{ with outer planetary pattern|}
      top=unusual {{long|short|pointy|round|protruding} [alienType] head{ with ant antennae and|} with {insect|humanoid|reptile|animal|bird|protruding} facial features, {{big black|small glowing|human|scary animal like|insect|} eyes^2|no eyes}, {{pointy elf|big round|elephant|human|} ears^2|no ears}, and {{beak for|trunk for^1.5|mandibles for|big|small|} nose^2|no nose}|no head}
      mid=[alienType] torso, {{butterfly|fairy|fly|dragon|bird|bat|} wings|{two|four} [alienType] arms^2}, 
      low={two|four} [alienType] legs{, {|long|medium|short} {fur|reptile|bird|monkey|insect} {|double |}tail|}
      rear=[this.top], [this.mid], [this.low]
    🤖Robot
      [robotType="{android|robot^2|cyborg|partially robotic [actorReference]|delivery bot|assembly shop robot|[actorList.gender[gender].selectOne] wearing exoskeleton}".evaluateItem,""]
      [/partially|wearing/i.test(robotType)?actorType="humanoid":actorType="mechanical",""][robotType][plural]
      {colorful|stainless steel^2|industrial|camouflage|urban|futuristic|no} paintjob
      {|oil {stains|leaks|drops}^0.5|{rust|dirt|dust|scratches|scuffs|damage} on the protection|}
      top=[/delivery|assembly/i.test(robotType)?"no face":actorType=="humanoid"?"human face":"{{analog monitor for|android|damaged with electronics showing|digital panel for|helmet like head with a single small eye socket for|human|metalic|robotic} face|no face}"]{|, radio antennae|, indicators|}
      mid=[robotType=="delivery bot"?"square container for body":robotType=="assembly shop robot"?"no body":actorType=="humanoid"?"stainless steel torso protection":"{aluminium|bionic|black iron|bronze|ceramic|glass|intricately designed with rib like horizontal armor plates along the|liquid metal|mechanical|plastic|synthetic|stainless steel} torso"], [robotType=="delivery bot"?"no arms":robotType=="assembly shop robot"?"assembly tools for hands, huge mechanical arms":actorType=="humanoid"?"human arms with steel protection":"{robotic|android|bionic|tools for|weapons for} arms{ with visible joints and cylindrical segments|}"]{|, panels|, cords|}
      low=[robotType=="delivery bot"?"wheels for legs":robotType=="assembly shop robot"?"no legs":actorType=="humanoid"?"human legs with steel protection":"{android|bionic|robotic|tracks for|wheels for} legs"]
      rear=[this.top], [this.mid], [this.low]
    <h3><b>saved</b></h3>
  gender
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="gender=this.value; updateDropdowns();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="gender" ${item.getName==gender?'checked':''} /><label>${item.getName}</label></div>`).join('')]
    ♀️Female
      subject=[actor=="🧑Person"?"":actor.lowerCase+[actorType=="humanoid"?" ":""]][actorType=="humanoid"?[age<=18?"girl":"female"]:""][plural]
      subjectSingular=[actor=="🧑Person"?"":actor.lowerCase+[actorType=="humanoid"?" ":""]][actorType=="humanoid"?[age<=18?"girl":"female"]:""]
      pronounPossessive=her
    ♂️Male
      subject=[actor=="🧑Person"?"":actor.lowerCase+[actorType=="humanoid"?" ":""]][actorType=="humanoid"?[age<=18?"boy":"male"]:""][plural]
      subjectSingular=[actor=="🧑Person"?"":actor.lowerCase+[actorType=="humanoid"?" ":""]][actorType=="humanoid"?[age<=18?"boy":"male"]:""]
      pronounPossessive=his
  bodyType
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="bodyType=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="bodyType" ${item.getName==bodyType?'checked':''} /><label>${item.getName=='Any body type'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any body type
    Athletic
      https://user.uploads.dev/file/85c7774ca9913268bfa19c4b95a4a2a0.webp
      very fit
    Average
      https://user.uploads.dev/file/7ac4a6e6122a3be755606dca6c289580.webp
      slightly unfit
      mid=medium height
      rear=[this.mid]
    Bodybuilder♂️
      https://user.uploads.dev/file/7acddc0807be6e7ff460c26056abf336.webp
      extra muscular
    Chubby
      https://user.uploads.dev/file/7731bec027af9717d6aa9caf04156669.webp
      extra fat
      low=big hips
      rear=[this.low][sceneExplicit?", chubby glutes":""]
    Curvy♀️
      https://user.uploads.dev/file/b620aadd98fb3919e1873238a6687056.webp
      fit
      mid=big chest
      low=big hips
      rear=[this.low][sceneExplicit?", big glutes":""]
    Overweight
      https://user.uploads.dev/file/ef82ba637e134674e2556e2ecd94d4fb.webp
      slightly more fat than average
      low=oversized hips
      rear=[this.low], oversized glutes
    Petite
      https://user.uploads.dev/file/d53a005078347fdd7f51dbfbc1335f10.webp
      fit
      mid=short, thin[gender=="♀️Female"?", flat"+[sceneExplicit?", dot-like chest":""]:""]
      low=thin hips[/merm/i.test(actor)?"":", thin thighs"]
      rear=short, thin, [this.low][sceneExplicit?", small glutes":""]
    Supermodel
      https://user.uploads.dev/file/cc6c2d22fd832c1ad83a1c383bca69d3.webp
      perfectly fit
      slender
      top=long neck
      mid=tall, perfect proportions, perfect posture
      low=[/merm/i.test(actor)?"long fish tail for legs":"long legs"]
      rear=[this.top], [this.mid], [this.low]
  ethnicity
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="ethnicity=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="ethnicity" ${item.getName==ethnicity?'checked':item.getName=='<h3><b>African</b></h3>'||item.getName=='<h3><b>Asian</b></h3>'||item.getName=='<h3><b>Caucasus</b></h3>'||item.getName=='<h3><b>Euro</b></h3>'||item.getName=='<h3><b>Indian</b></h3>'||item.getName=='<h3><b>Indigenous</b></h3>'||item.getName=='<h3><b>Latino</b></h3>'||item.getName=='<h3><b>Middle-eastern</b></h3>'||item.getName=='<h3><b>Slavic</b></h3>'?'disabled':''} /><label>${item.getName}</label></div>`).join('')]
    Any ethnicity
    <h3><b>African</b></h3>
    🌍African
      {African|Bantu|Berber|Bushman|Ethiopian|Fulani|Hausa|Igbo|Khoisan|Maasai|Nubian|Oromo|Somali|Yoruba|Zulu}
    Bantu
    Berber
    Bushman
    Ethiopian
    Fulani
    Hausa
    Igbo
    Khoisan
    Maasai
    Nubian
    Oromo
    Somali
    Yoruba
    Zulu
    <h3><b>Asian</b></h3>
    🌏Asian
      {Asian|Altai|Buryat|Cambodian|Chinese|Dai|Filipino|Hmong|Japanese|Kazakh|Khmer|Korean|Kyrgyz|Laotian|Mongolian|Taiwanese|Thai|Tibetan|Uyghur|Uzbek|Vietnamese|Yakut}
    Altai
    Buryat
    Cambodian
    Chinese
    Dai
    Filipino
    Hmong
    Japanese
    Kazakh
    Khmer
    Korean
    Kyrgyz
    Laotian
    Mongolian
    Taiwanese
    Thai
    Tibetan
    Uyghur
    Uzbek
    Vietnamese
    Yakut
    <h3><b>Caucasus</b></h3>
    ⛰Caucasus
      {Caucasus|Abkhaz|Adyghe|Armenian|Azerbaijani|Chechen|Circassian|Georgian|Ingush|Kabardian|Karachay|Ossetian|Svan|Tatar|Ubykh}
    Abkhaz
    Adyghe
    Armenian
    Azerbaijani
    Chechen
    Circassian
    Georgian
    Ingush
    Kabardian
    Karachay
    Ossetian
    Svan
    Tatar
    Ubykh
    <h3><b>Euro</b></h3>
    🌍Western European
      {Western European|Anglosaxon|British|Celtic|Danish|Dutch|French|German|Greek|English|Hispanic|Iberian|Irish|Italian|Norwegian|Portuguese|Scandinavian|Scottish|Swedish|Swiss|Welsh}
    Anglosaxon
    British
    Celtic
    Danish
    Dutch
    Irish
    French
    German
    Greek
    English
    Hispanic
    Iberian
    Irish
    Italian
    Norwegian
    Portuguese
    Scandinavian
    Scottish
    Swedish
    Swiss
    Welsh
    <h3><b>Indian</b></h3>
    🛕Indian
      {Indian|Bengali|Gujarati|Kashmiri|Marathi|Punjabi|Tamil|Telugu|Urdu}
    Bengali
    Gujarati
    Kashmiri
    Marathi
    Punjabi
    Tamil
    Telugu
    Urdu
    <h3><b>Indigenous</b></h3>
    🌎Indigenous tribes
      {Indigenous tribes|Aboriginal|Ainu|Aleut|Apache|Arapaho|Aymara|Aztec|Cherokee|Comanche|Guarani|Haida|Hopi|Inca|Inuit|Iroquois|Lakota|Mapuche|Maya|Navajo|Quechua|Sioux|Tlingit|Tupi|Zuni}
    Aboriginal
    Ainu
    Aleut
    Apache
    Arapaho
    Aymara
    Aztec
    Cherokee
    Comanche
    Guarani
    Haida
    Hopi
    Inca
    Inuit
    Iroquois
    Lakota
    Mapuche
    Maya
    Navajo
    Quechua
    Sioux
    Tlingit
    Tupi
    Zuni
    <h3><b>Latino</b></h3>
    🌎Latino
      {Latino|Argentinian|Brazilian|Chilean|Colombian|Cuban|Dominican|Mexican|Peruvian|Puerto Rican|Salvadoran|Venezuelan}
    Argentinian
    Brazilian
    Chilean
    Colombian
    Cuban
    Dominican
    Mexican
    Peruvian
    Puerto Rican
    Salvadoran
    Venezuelan
    <h3><b>Middle-eastern</b></h3>
    🕌Middle-eastern
      {Middle-eastern|Arab|Afghan|Assyrian|Bedouin|Iranian|Israeli|Kurdish|Lebanese|Palestinian|Persian|Sirian|Turkish|Egyptian}
    Arab
    Afghan
    Assyrian
    Bedouin
    Iranian
    Israeli
    Kurdish
    Lebanese
    Palestinian
    Persian
    Sirian
    Turkish
    Egyptian
    <h3><b>Slavic</b></h3>
    🏰Eastern European
      {Eastern European|Baltic|Belorussian|Bulgarian|Czech|Estonian|Latvian|Lithuanian|Polish|Russian|Serbian|Slavic|Slovak|Slovenian|Ukrainian}
    Baltic
    Belorussian
    Bulgarian
    Czech
    Estonian
    Latvian
    Lithuanian
    Polish
    Russian
    Serbian
    Slavic
    Slovak
    Slovenian
    Ukrainian
  aesthetic
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="aesthetic=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="aesthetic" ${item.getName==aesthetic?'checked':''} /><label>${item.getName}</label></div>`).join('')]
    Any aesthetic
    Adorable
      innocent and playful demeanor
    Average looking
    Beautiful♀️
      symmetrical, aesthetically pleasing and attractive features
    Cute
      attractive features in {a} {youthful|endearing} way, aesthetically pleasing
    Feminine♀️
      pronounced feminine, motherly aesthetically pleasing features, soft jawline
    Gorgeous
      perfectly symmetrical, aesthetically pleasing strikingly beautiful face
    Handsome♂️
      symmetrical, aesthetically pleasing and attractive masculine features
    Masculine♂️
      pronounced masculine, fatherly aesthetically pleasing features, strong jawline
    Plain looking
      asymmetrical features
    Pretty♀️
      aesthetically pleasing features
    Ugly
      asymmetrical disgusting features
      unevenly protruding forhead and jaws
      ["{crooked {nose|jaw}|uneven teeth|oversized {ears|nose}|}".evaluateItem]
 //<=Actor
eyesList // eye wear
  eyeWear
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="eyeWear=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="eyeWear" ${item.getName==eyeWear?'checked':''} /><label>${item.getName == 'Any eyewear' ? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any eyewear
    Blindfold
      https://user.uploads.dev/file/521a940b651573ad8d9ed7bf05a9eef8.webp
      top=blindfold
      rear=straps of a [this.top] on the back of the head
    Eye patch♂️
      https://user.uploads.dev/file/f2a0c0cc88671b0adb62b2db811e5e68.webp
      top=eye patch
      rear=straps of a [this.top] on the back of the head
    Goggles
      https://user.uploads.dev/file/1fb8bdbb21ad41849dd3cbe8f588448c.webp
      top=goggles
      rear=straps of a [this.top] on the back of the head
    Round glasses
      https://user.uploads.dev/file/8bdb635408bfbf2ea3376a88601e0bbc.webp
      top=round glasses
      rear=tips of a [this.top] on the ears
    Round sunglasses
      https://user.uploads.dev/file/8ffd5de4c586a92f63963a632c2b4465.webp
      top=round sunglasses
      rear=tips of a [this.top] on the ears
    Square glasses
      https://user.uploads.dev/file/100f77319ef239ec8cc2c643b02519a5.webp
      top=square glasses
      rear=tips of a [this.top] on the ears
    Square sunglasses
      https://user.uploads.dev/file/dc7dbc98e36a7560b27637ba9a870673.webp
      top=square sunglasses
      rear=tips of a [this.top] on the ears
    VR set
      https://user.uploads.dev/file/690d4ae449fe4b8c1b41914f0e59304f.webp
      top=VR set
      rear=double row of straps of a [this.top] on the back of the head
 //<=Eyes
hairList // hair length, style and body hair
  hairLength
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="hairLength=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="hairLength" ${item.getName==hairLength ? 'checked' : ''} /><label>${item.getName=='Any length' ? '' : '<img src='+item+'>'}${item.getName}</label></div>`).join('')]
    Any length
    Long
      https://user.uploads.dev/file/2abe36d4df7bbb210a8d07b3dc54a0ff.webp
    Medium
      https://user.uploads.dev/file/696ca9923c2bfec15b2d69260d23b247.webp
    Short
      https://user.uploads.dev/file/c3f676387b09dec36b721667d72c8365.webp
    Bald♂️
      https://user.uploads.dev/file/904bcf5dcc78745965bf307bef31c23e.webp
  hairStyle
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="hairStyle=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="hairStyle" ${item.getName==hairStyle?'checked':''} /><label>${item.getName == 'Any hairstyle'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any hairstyle
    Afro
      https://user.uploads.dev/file/ac6718a57006c965809677b4bcd6b40e.webp
    Bob
      https://user.uploads.dev/file/bca19a01688d487e4ddb4111d962f2d5.webp
    Braid♀️
      https://user.uploads.dev/file/13546ac4ed1b3bba4838bc17763b444c.webp
    Bun♀️
      https://user.uploads.dev/file/a1d2d9bf65a8eeec753d0cf47df88f6d.webp
    Crown♀️
      https://user.uploads.dev/file/b9de667bc11241a667228c64c9070bd1.webp
      loose elegant braid wraps around the head and is pinned up in a soft, voluminous bun reminding a crown
    Curly
      https://user.uploads.dev/file/921f922255dc8c3f6a2381edba44c675.webp
    Dreadlocks
      https://user.uploads.dev/file/66cda8dcabdbbf83e339698e4269e40b.webp
    Messy
      https://user.uploads.dev/file/838fc2b1c4dc79df02fe31ebe9bbba4b.webp
      messy bed hair
    Micro Braids
      https://user.uploads.dev/file/2903b331196a2429bc795c6e0d091b62.webp
    Mohawk
      https://user.uploads.dev/file/a462ce28fcaf3725384ef6358d8ec98d.webp
    Pixie
      https://user.uploads.dev/file/cfbea8628228c1b03ce170e4563db49b.webp
    Ponytail
      https://user.uploads.dev/file/7a5e170eca716c227dc925b9afd076df.webp
    Sidecut
      https://user.uploads.dev/file/782abc43e327dcb33ae6810027e33145.webp
    Spiky
      https://user.uploads.dev/file/9105b334bd5ef734cc627b40b5a2e36a.webp
    Square
      https://user.uploads.dev/file/f8795de57b80bd301b03a2914f9d8d1f.webp
    Straight
      https://user.uploads.dev/file/f6c7ef9d975cdbec88f8dad1fb3b3e26.webp
    Twintails♀️
      https://user.uploads.dev/file/a586f7bae7fee53278bd23fca04a602c.webp
    Two buns♀️
      https://user.uploads.dev/file/4a0585dcc229719a1887002f263a374a.webp
    Undercut
      https://user.uploads.dev/file/26f64dba9b146f0ed48c080a5efda118.webp
      faded undercut with shaved sides and back of the head
    Wavy
      https://user.uploads.dev/file/df8718201171c0f8d6ddc5a7e6ca8982.webp
  hairBody
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="hairBody=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="hairBody" ${item.getName==hairBody?'checked':''} /><label>${item.getName=='Any body hair'||item.getName=='No body hair'?'': '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any body hair
    No body hair
    Beard♂️
      https://user.uploads.dev/file/2640d5e60043f0c5af10c7adba5542dd.webp
      top=beard
    Chest♂️
      https://user.uploads.dev/file/75c0d22586f3a8dcdd4f0cb59ff5dcd1.webp
      mid=abundant chest hair
    Goatee♂️
      https://user.uploads.dev/file/63352ea7b650bc4f81001a3a46fd4ff4.webp
      top=goatee
    Mustache♂️
      https://user.uploads.dev/file/f967533c00b5459e1cde96c2665c5b39.webp
      top=mustache
    Pubes♀️
      https://user.uploads.dev/file/5f96c07f2c67f8a6ac2b83f6f5272755.webp
      low=abundant pubic hair
 //<=Hair
clothingList // clothing top, bottom, footwear, headwear, accessories, pattern
  Top
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️'):!item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="clothingTop=this.value;updateClothingVisibility();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="clothingTop" ${item.getName==clothingTop?'checked':item.getName == '<h3><b>Full suit</b></h3>'||item.getName == '<h3><b>Top</b></h3>'?'disabled':''} /><label>${item.getName == 'Any top'||item.getName == 'Any clothes'||item.getName == 'No clothes'||item.getName == 'No top'||item.getName == '<h3><b>Full suit</b></h3>'||item.getName == '<h3><b>Top</b></h3>'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any clothes
    No clothes
    <h3><b>Full suit</b></h3>
    Ballerina♀️
      https://user.uploads.dev/file/b0f195c9b20eedbe737e89a8cb789913.webp
      mid=ballerina leotard, ballerina tutu
      low=ballerina tights, ballerina flats with ribbons tied around the ankles
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Bath towel
      https://user.uploads.dev/file/ca9cc470334063be5907564110e133a3.webp
      top=bath towel on the head
      mid=bath towel
      low=bath slippers
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Batman♂️
      https://user.uploads.dev/file/72f6e88480c7c5e603e047972028009b.webp
      top=batman mask
      mid=batman suit with batman logo on the chest, batman gloves, batman belt
      low=batman pants, batman boots, partially visible batman cape on the sides
      rear=batman cape, mask straps on the back of the head
    Bodysuit
      https://user.uploads.dev/file/decd2e73c83807c9473b9c3e81c6cbc0.webp
      mid=bodysuit top, gloves
      low=bodysuit bottom, shoes
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Bride♀️
      https://user.uploads.dev/file/54833d92feddf3bef77e084a0f5f7155.webp
      top=bridal white veil
      mid=bridal dress, bouquet of roses in the [sceneHandsFree?"hands":"background"]
      low=white stockings, shoes
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Casual wear
      https://user.uploads.dev/file/6535bbcc11c72453ae2a03f7c0085cac.webp
      top={casual {baseball |}cap|}
      mid=casual {hoodie|shirt|t-shirt|sweater|jacket|coat}
      low=casual {jeans|pants|shorts|skirt|trousers}, casual everyday shoes
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Catwoman♀️
      https://user.uploads.dev/file/2c43b0c1a0b7dcf3422d7456a91b6a6a.webp
      top=catwoman mask
      mid=catwoman suit, catwoman gloves
      low=catwoman suit lower part, catwoman boots
      rear=[camera=="low-rear"?"":"[this.mid]"], catwoman mask straps on the back of the head
    Cheerleader♀️
      https://user.uploads.dev/file/8d0ba45f02fdd16db7aa3a61cad08ff3.webp
      mid=cheerleader top, cheerleader skirt, cheerleader pom-poms
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Construction
      https://user.uploads.dev/file/ba5304bd2d6516d074605a0dd733e21f.webp
      top=construction helmet
      mid=construction uniform, construction gloves
      low=construction boots
      rear=construction helmet, construction uniform
    Cowboy
      https://user.uploads.dev/file/bb57ad2f6d0858e29cd20a5a8c909b5a.webp
      top=cowboy hat
      mid=cowboy white shirt, belt, curled cowboy whip on the belt
      low=cowboy jeans, leather boots with spurs
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Detective♂️
      https://user.uploads.dev/file/99333f2514bdf6feab43fe9ce4514644.webp
      top=detective hat
      mid=detective coat, detective gloves, detective's magnifying glass
      low=detective boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Doctor
      https://user.uploads.dev/file/c4fee83ff6da77367da998741d34d492.webp
      mid=doctor white coat, doctor stethoscope
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Firefighter♂️
      https://user.uploads.dev/file/a2583fc1e3d0d275ec6d52f46d6815be.webp
      top=firefighter helmet
      mid=firefighter gloves, firefighter uniform
      low=firefighter boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"] with a fire extinguisher on the back
    Flight attendant♀️
      https://user.uploads.dev/file/c449649b8da5e3445f244ad812ca6be9.webp
      top=flight attendant headwear
      mid=flight attendant uniform
      low=flight attendant skirt, black stockings, shoes
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Football player
      https://user.uploads.dev/file/d94364a4a062ec3cec0ea5bf20945cba.webp
      top=football helmet
      mid=football uniform, football gloves
      low=football boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Formal wear
      https://user.uploads.dev/file/2408298e4c380e7e6fdd4331b1d859bf.webp
      mid=formal wear, white shirt, black jacket
      low=formal pants, formal shoes
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Geisha♀️
      https://user.uploads.dev/file/200886d0b40dfeb948768f77c55b2bf5.webp
      top=geisha headwear with geisha hair bun
      mid=geisha kimono
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Gothic wear
      https://user.uploads.dev/file/a81cd6dafc482693568767bddfb3fb1d.webp
      top=[gender=="♂️Male"?"black top hat":"black veil"]
      mid=gothic attire, black gloves, black umbrella[gender=="♀️Female"?", black corset":""]
      low=[gender=="♂️Male"?"black pants, walking stick":"black skirt"]
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Graduate
      https://user.uploads.dev/file/74c5b44294ea481eecc26131ace286ad.webp
      top=graduate cap
      mid=graduate gown
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Gymnast
      https://user.uploads.dev/file/c6e86ee594461910c933004822781d9d.webp
      mid=gymnast leotard
      low=gymnast leggings
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Hanbok
      https://user.uploads.dev/file/4fc39955140f7062f43026be8d20fc53.webp
      mid=hanbok
      low=shoes[sceneWet?" on a wooden platform":""]
      rear=hanbok
    High fasion wear
      https://user.uploads.dev/file/52cf9f3371781ddd1c49bf8a894b648b.webp
      mid=high fashion designer clothing
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Inmate
      https://user.uploads.dev/file/62995972954b3797f6228afe5545b5a3.webp
      mid=inmate uniform, inmate number on the chest
      low=inmate pants, inmate shoes
      rear=inmate uniform[camera=="mid-rear"?"":", [this.low]"]
    Judge
      https://user.uploads.dev/file/b2c04d4d6cfd55f37d731ebd16561475.webp
      mid=judge robe, [actorHandsFree?"holding a gavel by the handle":[/edge/i.test(sceneDimestions)?"gavel on the "+scene.lowerCase:""]]
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Kimono
      https://user.uploads.dev/file/ad8333b3a1ec104696ddd4334027225f.webp
      mid=kimono
      low=sandals
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Kisen♀️
      https://user.uploads.dev/file/9d9845b846ad8ddbaf7f2c2cbb701259.webp
      top=kisen wig with many pins and decorations
      mid=kisen hanbok, [sceneHandsFree?"kisen's traditional {musical instrument|fan}":""]
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Latex suit
      https://user.uploads.dev/file/9b539de21bad114d704fcd01824b978b.webp
      mid=latex suit, latex gloves
      low=latex boots
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Leather suit
      https://user.uploads.dev/file/56e0bd0c1be005cef7f97e0ca0769004.webp
      mid=leather jacket, leather gloves
      low=leather boots, leather hot pants
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Lolita♀️
      https://user.uploads.dev/file/d90ed84ea5a9c3827b0677dc8598e053.webp
      top=bow-tie headwear
      mid=blue laced dress with a wide rim, red bow-tie, white laced blouse, white long gloves
      low=white laced stockings, white laced [age>=18?"":"under"]panties, shoes with bows
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Maid♀️
      https://user.uploads.dev/file/9f2ead40e2e193d5fd014577de2daf2a.webp
      top=maid headwear
      mid=maid uniform, white blouse
      low=short black skirt, maid stockings, maid shoes
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Mandalorian♂️
      https://user.uploads.dev/file/8e9ff5326b2778924007c8ebce0d7bb4.webp
      top=mandalorian helmet
      mid=mandalorian suit, mandalorian gloves
      low=mandalorian boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Martial Artist
      https://user.uploads.dev/file/a64e97e558cdf64b490f42827abb6f00.webp
      mid={karate kimono|taekwondo tabok|fencing suit|boxing shorts, boxing gloves|kendo suit, kendo stick|judo kimono|wrestling singlet}
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Medieval armor
      https://user.uploads.dev/file/1785933aeea2448b3bfd134b9427d417.webp
      top=medieval helmet
      mid=medieval armor, medieval arm protection, medieval armored gloves, sword and shield
      low=medieval leg protection
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Medieval attire
      https://user.uploads.dev/file/284448cf5bfedd02836b8b86a8aa9642.webp
      mid=medieval [vibe=="Luxury"?"royal attire":"{attire|peasant rags|everyday robe|trader attire|noble attire|royal attire}"]
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Military
      https://user.uploads.dev/file/10d432fba5d7a92509b373b0eb2029ce.webp
      top=military combat helmet
      mid=military uniform, military jacket, military ballistic vest, assault rifle
      low=military pants, military boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Nightwear
      https://user.uploads.dev/file/2bd055ef5596778be2ab9131ff9ed012.webp
      mid=night {robe|pyjamas}
      low=nightwear slippers
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Ninja
      https://user.uploads.dev/file/496dd1763955e3a73cf97a3753f4f296.webp
      top=ninja mask
      mid=ninja suit, ninja gloves
      low=ninja soft boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Nun♀️
      https://user.uploads.dev/file/356a2e6e7d8cf833ff78ad027d72ab65.webp
      top=nun headwear
      mid=nun robe
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Nurse♀️
      https://user.uploads.dev/file/25b214549a3b2d795847d9a32e3f8e47.webp
      top=nurse headwear with the cross
      mid=nurse uniform
      low=white stockings, shoes
      rear=nurse headwear[camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Office
      https://user.uploads.dev/file/278be8be52761f3dcd543344f4c5d5e4.webp
      mid=office uniform, office suit, office jacket
      low=office [gender="♀️Female"?"skirt":"pants"], office shoes
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Outerwear
      https://user.uploads.dev/file/f6659ca5968dffd760a6396fa59b7f7c.webp
      top=[sceneCold?"fur-lined":sceneWet?"rain":sceneHot?"light":"warm"] hat{ with a coat hood on top|}[sceneCold?"":", scarf"]
      mid=[sceneCold?"fur-lined":sceneWet?"rain":sceneHot?"light":"warm"] outerwear[sceneCold?"":", {gloves|mittens}"]
      low=[sceneCold?"fur-lined":sceneWet?"rain":sceneHot?"light":"warm"] boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Pilot
      https://user.uploads.dev/file/1639c0b11e85ce6908cd0e3cc47afc5a.webp
      top=pilot cap
      mid=pilot uniform, pilot gloves
      low=pilot boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Pirate♂️
      https://user.uploads.dev/file/f3402bc580ec81bb374ce87e78d55065.webp
      top=pirate hat, pirate black eyepatch
      mid=pirate suit, pirate sabre, pirate pistol
      low=pirate pants, leather boots
      rear=pirate hat[camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Prehistoric
      https://user.uploads.dev/file/8f46091d3ad4058dfd45945cdb0be30d.webp
      mid=strips of leather and fur barely covering the [holeReference], stripped of any other clothing
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Police
      https://user.uploads.dev/file/eb1f54d669d9ce6a33f396bce8be77fa.webp
      top=police cap
      mid=police uniform, police badge, police handcuffs on the belt, police radio, police baton
      low=police pants, police boots
      rear=[camera=="low-rear"?"":this.top], police uniform, police, batton[camera=="mid-rear"?"":", [this.low]"]
    Robe
      https://user.uploads.dev/file/39fc99c7345ef2ac66d0b075ca88012b.webp
      top={robe hood up|}
      mid={mage|monk|priest|wizard|witch} robe
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Sailor♂️
      https://user.uploads.dev/file/e6c4ecafb41bedbeb44cc41741ecf7e6.webp
      top=sailor hat
      mid=sailor suit, sailor gloves
      low=sailt pants
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Samurai♂️
      https://user.uploads.dev/file/e265e7a59145e00784791457ca2e756f.webp
      top=samurai helmet
      mid=samurai armor
      low=samurai boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Santa
      https://user.uploads.dev/file/b58e1ac565845039d8d3d04d9ea1c295.webp
      top=santa hat
      mid=santa suit, santa gloves
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    School♀️
      https://user.uploads.dev/file/9e8e2c286968344dd8c45f4a5ce0bd63.webp
      mid=black school uniform, white blouse, bow-tie
      low=short brown tartan skirt
      rear=black school uniform[camera=="mid-rear"?"":", [this.low]"]
    Scuba diver
      https://user.uploads.dev/file/c1d2c810310a624a257d52bad7ddcafe.webp
      top=scuba diver mask
      mid=scuba diver bodysuit
      low=scuba diver flippers
      rear=straps of the [camera=="low-rear"?"":this.top] on the back of the head[camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Secretary♀️
      https://user.uploads.dev/file/d0d89f94a21f05f894dac0cc96051e7b.webp
      mid=secretary uniform, white blouse
      low=black long skirt, shoes
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Slave
      https://user.uploads.dev/file/1b8fc9fcc97a82eed051f80a3d4bf21b.webp
      mid=slave rags, slave shackles around the wrists, robe around the waist
      low=slave shackles around the ankles
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Spacesuit
      https://user.uploads.dev/file/f74cc70ba853bed0fde970fea23b5454.webp
      top=space helmet with open visor
      mid=spacesuit, space gloves
      low=space boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Spiderman♂️
      https://user.uploads.dev/file/9b573721faa3b6491c62cdeacaaa83c9.webp
      top=spiderman mask
      mid=spiderman bodysuit with spider web pattern, spiderman gloves
      low=spiderman boots
      rear=[camera=="low-rear"?"":this.top], spiderman bodysuit back[camera=="mid-rear"?"":", [this.low]"]
    Sportswear
      https://user.uploads.dev/file/23c6705629bd5676c79bf3aae3163375.webp
      mid={sports top|track suit top}
      low={sports shorts|track suit pants}, sneakers
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Superman♂️
      https://user.uploads.dev/file/7cb0625122c52559540d1f5f1cb386e0.webp
      mid=superman suit
      low=superman boots, partially visible superman cape on the sides
      rear=superman cape
    Stuardess♀️
      https://user.uploads.dev/file/86f11446a971a62d56452ad42ce586cf.webp
      top=stewardess headwear
      mid=stewardess uniform
      low=stewardess skirt
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Swimsuit♀️
      https://user.uploads.dev/file/2511171c3c22a577fbaa20a9d24dfd43.webp
      mid=swimsuit{ full piece|}
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Teacher♀️
      https://user.uploads.dev/file/f1388f78ea85b837c1beb896184844e2.webp
      mid=teacher blouse
      low=black long skirt
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Toxido♂️
      https://user.uploads.dev/file/887f657cd3ef2b8eb2899c91ea2a5bd6.webp
      mid=toxido, white shirt, black jacket, bow-tie
      low=black pants, black shoes
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Tracksuit
      https://user.uploads.dev/file/ed63238968f0149cbe6aa4ea006a5c0b.webp
      mid=tracksuit top
      low=tracksuit bottom, sneakers
    Traditional wear
      https://user.uploads.dev/file/e5365f0fde5bfb0348ae354788ae8d31.webp
      top=[ethnicity=="Any ethnicity"?tribal:ethnicity+" traditional headwear"]
      mid=[ethnicity=="Any ethnicity"?tribal:ethnicity+" traditional wear"]
      low=[ethnicity=="Any ethnicity"?tribal:ethnicity+" traditional footwear"]
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Trenchcoat
      https://user.uploads.dev/file/604040b919005ae5af0679cc4ab5f1d7.webp
      mid=trenchcoat, gloves
      low=boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Waitress♀️
      https://user.uploads.dev/file/dce63ccec9f0a7e2542a36297932a1f6.webp
      top=waitress restaraunt cap
      mid=waitress uniform, waitress apron
      low=waitress skirt
      rear=[camera=="low-rear"?"":this.top], waitress uniform[camera=="mid-rear"?"":", [this.low]"]
    Whore♀️
      https://user.uploads.dev/file/27f9d2b1b7bcbbadc8dc77345a5b64c4.webp
      top={cat|bunny} ears headband, dog collar
      mid={{crop|tube|mini} top|revealing {blouse|t-shirt|shirt} with plunging neckline}
      low={mini|short} skirt, {fishnet |}stockings, strings, high heels
      rear={cat|bunny} ears headband, {{crop|tube|mini} top|{blouse|t-shirt|shirt}}[camera=="mid-rear"?"":", [this.low]"]
    Witch
      https://user.uploads.dev/file/a9974accfc8fddcc66793d7fa550f2c4.webp
      top=witch hat
      mid=witch robe, [sceneHandsFree?"{holding|riding} a witch broom":""]
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"]
    Wonderwoman♀️
      https://user.uploads.dev/file/edc1e74fc535d15ab6031c413271b324.webp
      top=wonder woman tiara
      mid=wonder woman suit
      low=wonder woman boots
      rear=[camera=="low-rear"?"":this.top][camera=="low-rear"?"":", [this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Yukata
      https://user.uploads.dev/file/064455959802a80add5ed9d2e0596cf2.webp
      mid=yukata
      low=sandals
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    <h3><b>Top</b></h3>
    Any top
    No top
    Blouse♀️
      https://user.uploads.dev/file/4256a1bcf1b0125c3b3d8ebe34ee1c0a.webp
      mid=blouse
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Crop top♀️
      https://user.uploads.dev/file/c0a1e0cdc1f0aaf54fc20ce4d9ccac5f.webp
      mid=crop top
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Dress♀️
      https://user.uploads.dev/file/9fd72e8f70e29f71ed31b2a878d4dd14.webp
      mid=evening dress with deep neckline
      rear=evening dress with a zipper on the back
    Fur coat
      https://user.uploads.dev/file/4cb29a542230b76c750956c375c2e00b.webp
      mid=fur coat
      rear=[this.mid]
    Hoodie
      https://user.uploads.dev/file/b9796a07ef6fc7819bd68765aee98bf4.webp
      mid=hoodie with drawstrings
      rear=hoodie
    Jacket
      https://user.uploads.dev/file/e20c9e70ccc10016d7c981c5d10accd4.webp
      mid=jacket
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Leather jacket
      https://user.uploads.dev/file/4dc5ef5138688fd1c8449fb2721180f6.webp
      mid=leather jacket
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Mini dress♀️
      https://user.uploads.dev/file/f184605037d4b4e0baf535d9ac1e0a7b.webp
      mid=mini dress
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Pencil dress♀️
      https://user.uploads.dev/file/9bbdaf88ebc69e7cc79dbc03e0c42a74.webp
      mid=pencil dress
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Polo shirt
      https://user.uploads.dev/file/9470c0aaadf5f2e2053a4e975906ccd0.webp
      mid=polo shirt
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Pullover
      https://user.uploads.dev/file/7610841923f28ac3f4a2d7be9cee4b96.webp
      mid=pullover
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Rolled up shirt
      https://user.uploads.dev/file/1ca51b0bee925cf60db24d470c9c5b33.webp
      mid=shirt with rolled up sleeves
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Shirt
      https://user.uploads.dev/file/8b084d939c786bb22351c7fe75a6e669.webp
      mid=shirt with buttons and long sleeves
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Sports top♀️
      https://user.uploads.dev/file/3b78d41df721ad61bed2302c6c061be5.webp
      mid=sports bra with a simple, modern design
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Sundress♀️
      https://user.uploads.dev/file/781634b948c9ca5b97fdb60e1096518f.webp
      mid=sundress
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Sweater
      https://user.uploads.dev/file/abf1f5deb60396d4dd8a13455f515733.webp
      mid=sweater
      rear=[camera=="low-rear"?"":"[this.mid]"]
    T-shirt
      https://user.uploads.dev/file/fe3d5e15aa4e8c78b592f6731a3868db.webp
      mid=t-shirt
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Tank top♀️
      https://user.uploads.dev/file/3215f8a48258611f019232ccdfd07184.webp
      mid=tank top
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Tracksuit top
      https://user.uploads.dev/file/ce7410175f1c3206c35430ded397d617.webp
      mid=tracksuit top with a zipper
      rear=tracksuit top
    Tube top♀️
      https://user.uploads.dev/file/3f5e8c0b0d47485fb13c161aff8a9619.webp
      mid=strapless, form-fitting tube top made of light fabric
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Turtleneck
      https://user.uploads.dev/file/cd0a5884de7373bf088bce547e5c66ab.webp
      mid=turtleneck
      rear=[camera=="low-rear"?"":"[this.mid]"]
  lingerieTop
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️'):!item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="lingerieTop=this.value;updateClothingVisibility();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="lingerieTop" ${item.getName==lingerieTop?'checked':''} /><label>${item.getName == 'Any top lingerie'||item.getName == 'No top lingerie'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any top lingerie
    No top lingerie
    Bikini top♀️
      https://user.uploads.dev/file/d3633d0e8f4b9af598bea8d880d06950.webp
      mid=bikini top
      rear=[camera=="low-rear"?"":"[this.mid]"] tied on the back
    Bra♀️
      https://user.uploads.dev/file/f8647f14f1537f32611a614fed10b3ac.webp
      mid=[age>=18?"bra":"upper undergarments"]
      rear=[camera=="low-rear"?"":"[this.mid]"] fastened on the back
    Bustier♀️
      https://user.uploads.dev/file/ef7684b4692db536f942dca520278c16.webp
      mid=bustier
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Camisole♀️
      https://user.uploads.dev/file/27d840b53bc84111fee6936bd39b5696.webp
      mid=silky camisole with thin spaghetti straps and a delicate lace trim along the neckline and chest area
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Corset♀️
      https://user.uploads.dev/file/7dffeda6a111a0e159a1b7018fa6269a.webp
      mid=corset
      rear=[camera=="low-rear"?"":"[this.mid]"] with lacing on the back
  Bottom
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="clothingBottom=this.value;updateClothingVisibility();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="clothingBottom" ${item.getName==clothingBottom?'checked':''} /><label>${item.getName == 'Any bottom'||item.getName == 'No bottom'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any bottom
    No bottom
    Bell-bottomed pants
      https://user.uploads.dev/file/926e621da4e818a53845e5ecd783f790.webp
    Cargo pants
      https://user.uploads.dev/file/e4f2c71a5afa24c8c8a380f6df7eedce.webp
    Cargo shorts
      https://user.uploads.dev/file/d1fb3ed334d2a2db84ef2baccc22d58c.webp
    Chinos
      https://user.uploads.dev/file/e1f5f27d139589ab08f92522740e2f77.webp
    Denim skirt♀️
      https://user.uploads.dev/file/4ef0c314190233d52fb2d39b31bcf967.webp
    Denim shorts♀️
      https://user.uploads.dev/file/0c8f50f5c59b6dc5a4bd5f614bab3d6c.webp
    Hot pants♀️
      https://user.uploads.dev/file/1a847b86b89665ee2696cb72837aaa20.webp
    Hot shorts♀️
      https://user.uploads.dev/file/8b90765934659089d0feb07a4e35d2b1.webp
    Jeans
      https://user.uploads.dev/file/cd594e2601a9105d9fe7c3febfc6b354.webp
    Leggings♀️
      https://user.uploads.dev/file/e989fc9dd13bf447bf8b659f3aa54ebf.webp
    Leather pants
      https://user.uploads.dev/file/5a90f8b3b582b0f7e930d96433861695.webp
    Long skirt♀️
      https://user.uploads.dev/file/e0b81a490c92e55aea256e71a9a2d999.webp
      long skirt with a slit on the side
    Mini skirt♀️
      https://user.uploads.dev/file/7fb8cbcda4d8912a07f54918745e394d.webp
    Pants
      https://user.uploads.dev/file/f9ab92a417598637b2143f66c87479d6.webp
    Pencil skirt♀️
      https://user.uploads.dev/file/deb56bd1453c67ca8d9cec23c389253e.webp
    Short skirt♀️
      https://user.uploads.dev/file/1eb35b7afbcdca073a651913facddc4f.webp
    Shorts
      https://user.uploads.dev/file/b70d4ccb0ea7d02136a1bdac16e9a45e.webp
    Skirt♀️
      https://user.uploads.dev/file/3ffbe88ee4456ec4d1d97f302d0d4561.webp
    Sports shorts
      https://user.uploads.dev/file/b86830589a60030bada80499fd32fb84.webp
    Tennis skirt
      https://user.uploads.dev/file/c7d9f36a30113479016be8277cc67956.webp
    Thermal bottom
      https://user.uploads.dev/file/c4f96596423aa3b1dca2f66be179dcf2.webp
    Tracksuit bottom
      https://user.uploads.dev/file/b70c76c7409f36aacea3bf7131e3760a.webp
    Trousers
      https://user.uploads.dev/file/0944325caf636d05bf5c947fca7a4904.webp
    Yoga pants
      https://user.uploads.dev/file/f8bdcef8c84a6b713dbd9b337c1f1771.webp
  lingerieBottom
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️'):!item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="lingerieBottom=this.value;updateClothingVisibility();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="lingerieBottom" ${item.getName==lingerieBottom?'checked':''} /><label>${item.getName == 'Any bottom lingerie'||item.getName == 'No bottom lingerie'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any bottom lingerie
    No bottom lingerie
    Bikini bottom♀️
      https://user.uploads.dev/file/2c86045dc23fbd5cc12ec06d73bb96fd.webp
    Boxers
      https://user.uploads.dev/file/d3fb87fbb9d04d010e8f63e3b6b1c674.webp
    Boyshorts
      https://user.uploads.dev/file/7cc5c72b2580478d1c29618273e9be7b.webp
    Briefs♂️
      https://user.uploads.dev/file/afb7448249830a20ee7aca6b37ccd973.webp
    Panties
      https://user.uploads.dev/file/4a1378c892d3197c7b1bf64d3c299d6e.webp
      [age>=18?"panties":"underpanties"]
    Strings♀️
      https://user.uploads.dev/file/9dce31adf928d81b34cfb094a7feddb1.webp
      {c-|g-|t-|v-}strings
    Thong♀️
      https://user.uploads.dev/file/5b5760805a726e647d2acf7dbdfffad3.webp
    Trunks
      https://user.uploads.dev/file/df916112398863f8295ddf166f720891.webp
  Legwear
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="legwear=this.value;updateClothingVisibility();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="legwear" ${item.getName==legwear?'checked':''} /><label>${item.getName=='Any legwear'||item.getName=='No legwear'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any legwear
    No legwear
    Fishnet♀️
      https://user.uploads.dev/file/9e0df4c637a5d2132bfd07fbd8f6663b.webp
      fishnet stockings
    Garter belt♀️
      https://user.uploads.dev/file/eb18085718be888c1fbc720a318b0d76.webp
      [age>=18?"garter belt":"legband"]
    Leg warmers♀️
      https://user.uploads.dev/file/39b7f3661df77eefbaac11db0f86f282.webp
    Pantyhose♀️
      https://user.uploads.dev/file/34371a1c083273975b27116725779fce.webp
      [age>=18?"pantyhose":"tights"]
    Socks
      https://user.uploads.dev/file/a547d535a5653d0123fed98ad7c45715.webp
    Stockings♀️
      https://user.uploads.dev/file/4cb694d60e35b75200c2a5341be60bb1.webp
    Thigh socks♀️
      https://user.uploads.dev/file/ee927a223fa47aaeab2520a2b318b692.webp
    Tights♀️
      https://user.uploads.dev/file/4087f5917fff5502c91fc98b9a78829e.webp
  Footwear
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="footwear=this.value;updateClothingVisibility();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="footwear" ${item.getName==footwear?'checked':''} /><label>${item.getName=='Any footwear'||item.getName=='No footwear'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any footwear
    No footwear
    Ballet flats♀️
      https://user.uploads.dev/file/eab9aeabc733231fc579d3b4e1eb3d38.webp
      ballet flats with ribbons tied around the ankles
    Boots
      https://user.uploads.dev/file/e98fc25cc0d65da49ec5ffd094b49b26.webp
    Clogs
      https://user.uploads.dev/file/ea992acf5cb3c4588d37734f154d80f7.webp
    Flip-flops
      https://user.uploads.dev/file/238eb65a5a7b80008a4356f04647c688.webp
    High heels♀️
      https://user.uploads.dev/file/3662d7bfa939916e080557ed4ebc840e.webp
    Loafers
      https://user.uploads.dev/file/21ea312e712764cdc92ca5b45d5450b9.webp
    Platforms♀️
      https://user.uploads.dev/file/94a3f82e035a548276cd3fae3deabc45.webp
      stylish, high-heeled, chunky platform sandals with thick, ridged soles and ankle straps
    Pumps♀️
      https://user.uploads.dev/file/9fbb983986ce064858bd12b2f434f7ef.webp
    Sandals
      https://user.uploads.dev/file/b92f1ce2855e595e6a4e3b161e2cf3ce.webp
    Shoes
      https://user.uploads.dev/file/f761b25e129d806c7196f942f1851097.webp
    Slippers
      https://user.uploads.dev/file/d5d1351383a930dc046643015985453a.webp
    Sneakers
      https://user.uploads.dev/file/7b45d48d674b6aaba556f189af9ef37c.webp
    Thigh boots
      https://user.uploads.dev/file/ccb69e0327f1ae953efcdc2f7b041c48.webp
  Headwear
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="headwear=this.value;updateClothingVisibility();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="headwear" ${item.getName==headwear?'checked':''} /><label>${item.getName=='Any headwear'||item.getName=='No headwear'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any headwear
    No headwear
    Bandana
      https://user.uploads.dev/file/17fd362a60a3c05a5d863ef2acc46290.webp
      bandana made of lightweight fabric with a pattern covering the head and tied at the back
    Beret
      https://user.uploads.dev/file/d031cc7380ed583f7d35f5dd940a7110.webp
    Bucket hat
      https://user.uploads.dev/file/234421cf3de86a29339836240d1c611b.webp
    Bunny ears♀️
      https://user.uploads.dev/file/d245e4e28464c81a215f67770e8b99df.webp
      {bunny|rabbit} ears headband
    Burqa♀️
      https://user.uploads.dev/file/10c35c53b1ac4a43f5d3f1a7f8e755e9.webp
    Cap
      https://user.uploads.dev/file/c4a40e82c1cf45f11ccf28127995761f.webp
    Cat ears♀️
      https://user.uploads.dev/file/adb68a0a11f96c78b4da14118909fddf.webp
      cat ears headband
    Cowboy Hat
      https://user.uploads.dev/file/333f60ba1c143098612769ef4a80d0c9.webp
    Crown
      https://user.uploads.dev/file/f6691d9f7600e69792fbe2379b9c5584.webp
      crown
    Earmuffs
      https://user.uploads.dev/file/8b57450bf57b1da99c0ad45b45a1204f.webp
    Fur hat
      https://user.uploads.dev/file/6d8a8e201ad4cafb7c82c8dbd0ea51c1.webp
    Hat
      https://user.uploads.dev/file/cf209d5ce1bd62246a23bfe25136daf5.webp
    Headband♀️
      https://user.uploads.dev/file/5eb52f6ff4239fc7cca0bf6aa236a291.webp
    Headlamp
      https://user.uploads.dev/file/4f20cc116a6fe192188aa085e2941b59.webp
      headlamp with big LED light[actor=="Any actor"?"":", secured to the head"]
    Headphones
      https://user.uploads.dev/file/a9ce64ad8b0fab18a8ff23cec637c643.webp
    Headscarf
      https://user.uploads.dev/file/606cbe6cb3c68169fcd50ce374e25389.webp
    Helmet
      https://user.uploads.dev/file/c9d828619cd71029cdf20e0958b2296f.webp
      {construction|safety} helmet
    Hijab♀️
      https://user.uploads.dev/file/da8518b8ba4be6aad6b52a2c842b383e.webp
    Motocycle helmet
      https://user.uploads.dev/file/55d508a3065e30c1fbccac6d9820530d.webp
    Party hat
      https://user.uploads.dev/file/127fad391c99e4ee16d1e6a670f6b0d1.webp
    Ribbon♀️
      https://user.uploads.dev/file/f6700c40a4ab011c952a0ff73e391857.webp
      ribbon in the hair
    Straw hat
      https://user.uploads.dev/file/f435e5bb9f16e97ec2ca49f58fdb355b.webp
    Sun hat
      https://user.uploads.dev/file/493a422ec7a22e00e7c8d94ad8e1c9c3.webp
    Tiara
      https://user.uploads.dev/file/9bc164e0e6a43b23a77fbc63b9d3d395.webp
    Tribal
      https://user.uploads.dev/file/05b88a3f0473e877c2e46a30a434154d.webp
      [tribal] headdress and mask
    Turban♂️
      https://user.uploads.dev/file/ab583e597f9b71613613be9fa50946c5.webp
    Wig
      https://user.uploads.dev/file/f3917d2f00796f77690218595fe817b4.webp
      renaissance style white wig with curls on the sides
  Accessories
    $output = [this.selectAll.filter(item => /bird|cat|dog|fox|horse|koala|monkey|mouse|panda|rabbit|unicorn|wolf/i.test(actor)? item.getName.includes('🐾')||item.getName=="Any accessories":item).filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️') : !item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="accessories=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="accessories" ${item.getName==accessories?'checked':''} /><label>${item.getName=='Any accessories'||item.getName=='No accessories'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any accessories
    No accessories
    Badge
      https://user.uploads.dev/file/111.webp
      mid=name badge on the left part of the chest
    Bag
      https://user.uploads.dev/file/9d97a992fe61f00a6296473a3cc07664.webp
      mid=bag [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Baseball bat
      https://user.uploads.dev/file/62c19b8e63d96ae18d044aa6fda009ce.webp
      mid=baseball bat [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[this.mid]
    Belt
      https://user.uploads.dev/file/bccc22c389347ff2c9b902b1329e2fae.webp
      mid=leather belt around the waist"
      rear=[this.mid]
    Blanket
      https://user.uploads.dev/file/bfe2f98e43cf9abe19d0aa74caaf7fdf.webp
      top=top part of the blanket covering the head creating a cosy space
      mid=blanket on the shoulders
      rear=[this.mid]
    Bow-tie
      https://user.uploads.dev/file/8261d5abb62d7f37b6bf443d46977399.webp
      top=bow-tie
      rear=[camera=="low-rear"?"":"straps of a bow-tie on the back of the neck"]
    Bracelet
      https://user.uploads.dev/file/9a941530cb6b15061363d2da0e3c6a98.webp
      mid=bracelet
      rear=[this.mid]
    Briefcase
      https://user.uploads.dev/file/1db45a834709fdd61b5e2e5cca68f681.webp
      mid=briefcase
      rear=[this.mid]
    Carnival mask
      https://user.uploads.dev/file/3df48e6c665855c64e2fc6966a164833.webp
      top={carnival|masquerade} mask
      rear=[camera=="low-rear"||camera=="mid-rear"?"":"straps of a mask on the back of the head"]
    Chains
      https://user.uploads.dev/file/e32f9ef5b31b49ca2af780b7e45c7d4c.webp
      mid=chain wrapped around the wrists
      low=chain wrapped around the [/merm/i.test(actor)?"fish tail":"ankles"]
      rear=[camera=="low-rear"?"":"[this.mid]"][camera=="mid-rear"?"":", [this.low]"]
    Coffee
      https://user.uploads.dev/file/79321847d9643705118ef7080e5f51bc.webp
      mid={cup|mug} of coffee [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[this.mid]
    Dildo♀️
      https://user.uploads.dev/file/2c84b07e15a21345c88dca9eaea36c74.webp
      mid=[age>=18?"dildo":"rubber shaft"] [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[this.mid]
    Dog collar🐾
      https://user.uploads.dev/file/d12124448cbf696acd4e4ffa2dee506c.webp
      top=dog collar
      rear=[this.top] fastened on the back of the neck
    Earrings
      https://user.uploads.dev/file/bffe592c666bd3d9d3391bf2d17af4f2.webp
      top=fancy earings
      rear=[camera=="low-rear"?"":"[this.top]"]
    Fan♀️
      https://user.uploads.dev/file/cf8e1b8ef8853fd7178ab68560be11d7.webp
      mid=folding fan [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[this.mid]
    Flowers
      https://user.uploads.dev/file/7606c9ce288b82b3c9894da15261c30f.webp
      mid=bouquet of flowers [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Gas mask
      https://user.uploads.dev/file/1e97f39b0ce1d9ed8c7c240f052efa15.webp
      top=gas mask
      rear=[camera=="low-rear"||camera=="mid-rear"?"":"straps of a mask on the back of the head"]
    Glass
      https://user.uploads.dev/file/7cd4a48655f155745f20863e4665f013.webp
      mid=glass of [(/romantic|18/i.test(vibe)||sceneExplicit)&&age>=18?"{beer|champaign|wine|whiskey}":"{gassed |}{water|juice}"] [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Gloves
      https://user.uploads.dev/file/957899121a14a986b50ff1d296ef36f7.webp
      mid=gloves
      rear=[this.mid]
    Halloween mask
      https://user.uploads.dev/file/6dd2020afb5bc8f0be57b9ae04d1a1b3.webp
      top={pumpking head|call movie|freddy krueger|ghostface|jason voorhees|michael myers} mask
      rear=[camera=="low-rear"||camera=="mid-rear"?"":"straps of a mask on the back of the head"]
    Handbag
      https://user.uploads.dev/file/83981aaced44efb67bf930a8e71eddab.webp
      mid=handbag [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[this.mid]
    Handcuffs
      https://user.uploads.dev/file/61a5d0daedbe60cf08f0ca340427e17e.webp
      mid=metal police [age>=18?"handcuffes":"bracelets"] securing both wrists, the handcuffs are fastened with a chain connecting the cuffs around both wrists, hands are clenched into fists
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Laptop
      https://user.uploads.dev/file/9b90fb74fd2877ddee1b4ee4736cd4c1.webp
      mid=laptop [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[this.mid]
    Leash🐾
      https://user.uploads.dev/file/9ed92663bb0f6456760781efc6ea6230.webp
      top=[actor=="🐴Horse"?"reins and a saddle":"leash fastened on the neck"+[view=="POV"?" controlled by the [POV]'s hand":""]]
      rear=[camera=="low-rear"?"":[actor=="🐴Horse and a saddle"?"reins":"leash fastened on the back of the neck"+[view=="POV"?" controlled by the [POV]'s hand":""]]]
    Magic wand
      https://user.uploads.dev/file/111.webp
      mid=magic wand [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[this.mid]
    Medical mask
      https://user.uploads.dev/file/c188c94248134a9d31d94c05a8447158.webp
      top=medical mask
      rear=[camera=="low-rear"||camera=="mid-rear"?"":"straps of a mask on the back of the head"]
    Mittens
      https://user.uploads.dev/file/e464572531f6c9625b32f2b90712fbd3.webp
      mid=knitted mittens with a complex, symmetrical pattern on the hands
      rear=[this.mid]
    Muzzle🐾
      https://user.uploads.dev/file/67860b117d771f000f9fb2abfe05b02d.webp
      top=[actor=="🐴Horse"?"bridle":"plastic muzzle with metal bars covering the mouth and nose secured with straps"]
      rear=[camera=="low-rear"?"":"muzzle straps on the back of the head"]
    Necklace
      https://user.uploads.dev/file/5c3fd0768e729ddc69bc73fcf8b7e295.webp
      top=necklace
      rear=[camera=="low-rear"?"":"[this.top] fastened on the back of the neck"]
    Ring
      https://user.uploads.dev/file/6e584855ac7146c49ed0ba10a7d4ef61.webp
      mid=ring
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Rope
      https://user.uploads.dev/file/87fb608966fe7fd268e5a50d71d754e0.webp
      mid=rope wrapped around the wrists
      low=rope wrapped around the [/merm/i.test(actor)?"fish tail":"ankles"]
      rear=[camera=="low-rear"?"":"[this.mid]"], [this.low]
    Scarf
      https://user.uploads.dev/file/390c8262c6b91ed20cdd55f9f1fa24c1.webp
      top=scarf
      mid=the scarf endings hanging on the chest
      rear=[camera=="low-rear"?"":"scarf endings on the side"]
    Shoulder bag
      https://user.uploads.dev/file/b1a52a8ab786c110967cc29434ad4808.webp
      mid=shoulderbag [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Slave attributes
      https://user.uploads.dev/file/8cdf1a4250bdeb7333a03147b483c201.webp
      top=slave collar
      mid=slave shackles, {rope|chain} wrapped around the wrists
      low={rope|chain} wrapped around the [/merm/i.test(actor)?"fish tail":"ankles"]
      rear=[camera=="low-rear"?"":"[this.top] fastened on the back of the neck"][camera=="low-rear"?"":", [this.mid]"], [this.low]
    Smartphone
      https://user.uploads.dev/file/a9c40aaa62a460b075387fadaa4436c7.webp
      mid=smartphone [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
      rear=[this.mid]
    Strap-on♀️
      https://user.uploads.dev/file/be24dd6328eef1a896dcb521331357a8.webp
      mid=[age>=18?"strap-on with a dildo":"plastic shaft"] on a belt fastened around the waist
      rear=belt fastened on the lower back
    Studs
      https://user.uploads.dev/file/e74d1cc2a411dc3e195ea3d4391758b5.webp
      top=studs
      rear=[camera=="low-rear"?"":"[this.top]"]
    Theatrical mask
      https://user.uploads.dev/file/fdf175f4e67316225c60c80f3d2d8a02.webp
      top={comedy|tragedy} mask
      rear=[camera=="low-rear"||camera=="mid-rear"?"":"straps of a mask on the back of the head"]
    Tie
      https://user.uploads.dev/file/4433afb7f32f4c98c033c44d5121300a.webp
      top=tie
      mid=the tie hanging down on the chest
    Tribal attributes
      https://user.uploads.dev/file/e4686382b0a9e3fa85ebeffde0529efa.webp
      top=[tribal] jewelry and feathers
      mid=[tribal] shamanic drum
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Umbrella
      https://user.uploads.dev/file/cd8d54c701c94d80e24791807e6fecfb.webp
      top=[sceneOpenAir?"open umbrella above the head":""]
      mid=[sceneOpenAir?"umbrella handle"+[sceneHandsFree?" in the hand":" under the armpit"]:"closed umbrella in the background"]
      rear=[camera=="low-rear"?"":"[this.top]"][camera=="low-rear"?"":", [this.mid]"]
    Wallet
      https://user.uploads.dev/file/a27414922a95e434b49b8a891f5b8374.webp
      mid=wallet [sceneHandsFree?"in hand":/edge/i.test(sceneDimension)?"on"+scene.lowerCase:"lying near [actorReference.subject]"]
    Watch
      https://user.uploads.dev/file/45d22823ad998e8b3b30e39b9dd9cf58.webp
      mid=watch on the {left |right |}wrist
      rear=[camera=="low-rear"?"":"[this.mid]"]
    Whip
      https://user.uploads.dev/file/3c562c644ed68d39fb672723df4912f7.webp
      mid=whip[sceneHandsFree?" in hand":/edge/i.test(sceneDimension)?" on"+scene.lowerCase:" coiled on [actorReference.subject] waist"]
      low=whip tip hanging down
      rear=[this.mid],[this.low]
  PatternTop
    $output=[this.selectAll.map(item => `<div><input value="${item.getName}" onchange="clothingTopPattern=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="clothingTopPattern" ${item.getName==clothingTopPattern?'checked':''} /><label>${'<img src='+item.selectAll[0]+'>'}</label></div>`).join('')]
    Plain
      https://user.uploads.dev/file/59731566979ab54d9f75735eb8a3cc36.png
    Argyle
      https://user.uploads.dev/file/78c3624c09ef2f630ffb0e9fa86187de.png
    Basketweave
      https://user.uploads.dev/file/624dbfb7c75e8324e80d18e73d64d26f.png
    Buffalo check
      https://user.uploads.dev/file/6da143eda0c0841a475c37247192cdea.png
    Camouflage
      https://user.uploads.dev/file/4cd9fb5899131b830bb9b651db0bbfc7.png
    Check
      https://user.uploads.dev/file/01882e259d33b7852d796cc86e315897.png
    Chevron
      https://user.uploads.dev/file/54e9d92fc917ec77123eeb13ce20a104.png
    Damask
      https://user.uploads.dev/file/a2cc415dd146160fcc92c112d1519fd2.png
    Floral
      https://user.uploads.dev/file/e45aef59f51c1f212d2c4a6749b3c004.png
    Fret
      https://user.uploads.dev/file/75f03deb92b565aac3e7c63bf67a2698.png
    Gingham
      https://user.uploads.dev/file/4570bc12209eab719a2d7a4590567160.png
    Herringbone
      https://user.uploads.dev/file/c0e304867077ef5e89b0ee17a47a46c1.png
    Honeycomb
      https://user.uploads.dev/file/28102a215027185528ebea447a519cec.png
    Houndstooth
      https://user.uploads.dev/file/186f8863cd393e8b790d5154447b0e68.png
    Ikat
      https://user.uploads.dev/file/b14a6d5b181443270c2af2114f96f55c.png
    Lattice
      https://user.uploads.dev/file/6cb6f9bc5041ff162284da60443b6c66.png
    Ornamented
      https://user.uploads.dev/file/306409d9aa865d7199157dd25deeca2b.png
    Pin-stripped
      https://user.uploads.dev/file/516488b644b16088ceece48a0d6b417f.png
    Polka dots
      https://user.uploads.dev/file/3389f07bc55f871b85212c26b40b039a.png
    Ripped
      https://user.uploads.dev/file/4e514e4c40e74dfb16412fa3bb5ec955.png
    Striped
      https://user.uploads.dev/file/5be9341db416c691f4ce39ad5d10a0c5.png
    Tartan
      https://user.uploads.dev/file/9696a0b8b6404129ccd55c07db6c474d.png
    Tie-died
      https://user.uploads.dev/file/ea26b44d9ab5c1c655978619373f6cf3.png
    Toile
      https://user.uploads.dev/file/83c3aa5afae0d1f254fd5e48fdb4c04e.png
    Tweed
      https://user.uploads.dev/file/14af17a65d60d576765afb89d0e17b80.png
    Wrinkled
      https://user.uploads.dev/file/111.png
    Zigzag
      https://user.uploads.dev/file/f713aaf36502efd281f320d53f1d3cf9.png
  PatternLingerieTop
    $output=[this.selectAll.map(item => `<div><input value="${item.getName}" onchange="lingerieTopPattern=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="lingerieTopPattern" ${item.getName==lingerieTopPattern?'checked':''} /><label>${'<img src='+item.selectAll[0]+'>'}</label></div>`).join('')]
    Plain
      https://user.uploads.dev/file/59731566979ab54d9f75735eb8a3cc36.png
    Argyle
      https://user.uploads.dev/file/78c3624c09ef2f630ffb0e9fa86187de.png
    Basketweave
      https://user.uploads.dev/file/624dbfb7c75e8324e80d18e73d64d26f.png
    Buffalo check
      https://user.uploads.dev/file/6da143eda0c0841a475c37247192cdea.png
    Camouflage
      https://user.uploads.dev/file/4cd9fb5899131b830bb9b651db0bbfc7.png
    Check
      https://user.uploads.dev/file/01882e259d33b7852d796cc86e315897.png
    Chevron
      https://user.uploads.dev/file/54e9d92fc917ec77123eeb13ce20a104.png
    Damask
      https://user.uploads.dev/file/a2cc415dd146160fcc92c112d1519fd2.png
    Floral
      https://user.uploads.dev/file/e45aef59f51c1f212d2c4a6749b3c004.png
    Fret
      https://user.uploads.dev/file/75f03deb92b565aac3e7c63bf67a2698.png
    Gingham
      https://user.uploads.dev/file/4570bc12209eab719a2d7a4590567160.png
    Herringbone
      https://user.uploads.dev/file/c0e304867077ef5e89b0ee17a47a46c1.png
    Honeycomb
      https://user.uploads.dev/file/28102a215027185528ebea447a519cec.png
    Houndstooth
      https://user.uploads.dev/file/186f8863cd393e8b790d5154447b0e68.png
    Ikat
      https://user.uploads.dev/file/b14a6d5b181443270c2af2114f96f55c.png
    Lattice
      https://user.uploads.dev/file/6cb6f9bc5041ff162284da60443b6c66.png
    Ornamented
      https://user.uploads.dev/file/306409d9aa865d7199157dd25deeca2b.png
    Pin-stripped
      https://user.uploads.dev/file/516488b644b16088ceece48a0d6b417f.png
    Polka dots
      https://user.uploads.dev/file/3389f07bc55f871b85212c26b40b039a.png
    Ripped
      https://user.uploads.dev/file/4e514e4c40e74dfb16412fa3bb5ec955.png
    Striped
      https://user.uploads.dev/file/5be9341db416c691f4ce39ad5d10a0c5.png
    Tartan
      https://user.uploads.dev/file/9696a0b8b6404129ccd55c07db6c474d.png
    Tie-died
      https://user.uploads.dev/file/ea26b44d9ab5c1c655978619373f6cf3.png
    Toile
      https://user.uploads.dev/file/83c3aa5afae0d1f254fd5e48fdb4c04e.png
    Tweed
      https://user.uploads.dev/file/14af17a65d60d576765afb89d0e17b80.png
    Wrinkled
      https://user.uploads.dev/file/111.png
    Zigzag
      https://user.uploads.dev/file/f713aaf36502efd281f320d53f1d3cf9.png
  PatternBottom
    $output=[this.selectAll.map(item => `<div><input value="${item.getName}" onchange="clothingBottomPattern=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="clothingBottomPattern" ${item.getName==clothingBottomPattern?'checked':''} /><label>${'<img src='+item.selectAll[0]+'>'}</label></div>`).join('')]
    Plain
      https://user.uploads.dev/file/59731566979ab54d9f75735eb8a3cc36.png
    Argyle
      https://user.uploads.dev/file/78c3624c09ef2f630ffb0e9fa86187de.png
    Basketweave
      https://user.uploads.dev/file/624dbfb7c75e8324e80d18e73d64d26f.png
    Buffalo check
      https://user.uploads.dev/file/6da143eda0c0841a475c37247192cdea.png
    Camouflage
      https://user.uploads.dev/file/4cd9fb5899131b830bb9b651db0bbfc7.png
    Check
      https://user.uploads.dev/file/01882e259d33b7852d796cc86e315897.png
    Chevron
      https://user.uploads.dev/file/54e9d92fc917ec77123eeb13ce20a104.png
    Damask
      https://user.uploads.dev/file/a2cc415dd146160fcc92c112d1519fd2.png
    Floral
      https://user.uploads.dev/file/e45aef59f51c1f212d2c4a6749b3c004.png
    Fret
      https://user.uploads.dev/file/75f03deb92b565aac3e7c63bf67a2698.png
    Gingham
      https://user.uploads.dev/file/4570bc12209eab719a2d7a4590567160.png
    Herringbone
      https://user.uploads.dev/file/c0e304867077ef5e89b0ee17a47a46c1.png
    Honeycomb
      https://user.uploads.dev/file/28102a215027185528ebea447a519cec.png
    Houndstooth
      https://user.uploads.dev/file/186f8863cd393e8b790d5154447b0e68.png
    Ikat
      https://user.uploads.dev/file/b14a6d5b181443270c2af2114f96f55c.png
    Lattice
      https://user.uploads.dev/file/6cb6f9bc5041ff162284da60443b6c66.png
    Ornamented
      https://user.uploads.dev/file/306409d9aa865d7199157dd25deeca2b.png
    Pin-stripped
      https://user.uploads.dev/file/516488b644b16088ceece48a0d6b417f.png
    Polka dots
      https://user.uploads.dev/file/3389f07bc55f871b85212c26b40b039a.png
    Ripped
      https://user.uploads.dev/file/4e514e4c40e74dfb16412fa3bb5ec955.png
    Striped
      https://user.uploads.dev/file/5be9341db416c691f4ce39ad5d10a0c5.png
    Tartan
      https://user.uploads.dev/file/9696a0b8b6404129ccd55c07db6c474d.png
    Tie-died
      https://user.uploads.dev/file/ea26b44d9ab5c1c655978619373f6cf3.png
    Toile
      https://user.uploads.dev/file/83c3aa5afae0d1f254fd5e48fdb4c04e.png
    Tweed
      https://user.uploads.dev/file/14af17a65d60d576765afb89d0e17b80.png
    Wrinkled
      https://user.uploads.dev/file/111.png
    Zigzag
      https://user.uploads.dev/file/f713aaf36502efd281f320d53f1d3cf9.png
  PatternLingerieBottom
    $output=[this.selectAll.map(item => `<div><input value="${item.getName}" onchange="lingerieBottomPattern=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="lingerieBottomPattern" ${item.getName==lingerieBottomPattern?'checked':''} /><label>${'<img src='+item.selectAll[0]+'>'}</label></div>`).join('')]
    Plain
      https://user.uploads.dev/file/59731566979ab54d9f75735eb8a3cc36.png
    Argyle
      https://user.uploads.dev/file/78c3624c09ef2f630ffb0e9fa86187de.png
    Basketweave
      https://user.uploads.dev/file/624dbfb7c75e8324e80d18e73d64d26f.png
    Buffalo check
      https://user.uploads.dev/file/6da143eda0c0841a475c37247192cdea.png
    Camouflage
      https://user.uploads.dev/file/4cd9fb5899131b830bb9b651db0bbfc7.png
    Check
      https://user.uploads.dev/file/01882e259d33b7852d796cc86e315897.png
    Chevron
      https://user.uploads.dev/file/54e9d92fc917ec77123eeb13ce20a104.png
    Damask
      https://user.uploads.dev/file/a2cc415dd146160fcc92c112d1519fd2.png
    Floral
      https://user.uploads.dev/file/e45aef59f51c1f212d2c4a6749b3c004.png
    Fret
      https://user.uploads.dev/file/75f03deb92b565aac3e7c63bf67a2698.png
    Gingham
      https://user.uploads.dev/file/4570bc12209eab719a2d7a4590567160.png
    Herringbone
      https://user.uploads.dev/file/c0e304867077ef5e89b0ee17a47a46c1.png
    Honeycomb
      https://user.uploads.dev/file/28102a215027185528ebea447a519cec.png
    Houndstooth
      https://user.uploads.dev/file/186f8863cd393e8b790d5154447b0e68.png
    Ikat
      https://user.uploads.dev/file/b14a6d5b181443270c2af2114f96f55c.png
    Lattice
      https://user.uploads.dev/file/6cb6f9bc5041ff162284da60443b6c66.png
    Ornamented
      https://user.uploads.dev/file/306409d9aa865d7199157dd25deeca2b.png
    Pin-stripped
      https://user.uploads.dev/file/516488b644b16088ceece48a0d6b417f.png
    Polka dots
      https://user.uploads.dev/file/3389f07bc55f871b85212c26b40b039a.png
    Ripped
      https://user.uploads.dev/file/4e514e4c40e74dfb16412fa3bb5ec955.png
    Striped
      https://user.uploads.dev/file/5be9341db416c691f4ce39ad5d10a0c5.png
    Tartan
      https://user.uploads.dev/file/9696a0b8b6404129ccd55c07db6c474d.png
    Tie-died
      https://user.uploads.dev/file/ea26b44d9ab5c1c655978619373f6cf3.png
    Toile
      https://user.uploads.dev/file/83c3aa5afae0d1f254fd5e48fdb4c04e.png
    Tweed
      https://user.uploads.dev/file/14af17a65d60d576765afb89d0e17b80.png
    Wrinkled
      https://user.uploads.dev/file/111.png
    Zigzag
      https://user.uploads.dev/file/f713aaf36502efd281f320d53f1d3cf9.png
 //<=Clothing
featuresList // tattoos, piercing, makeup, nails, condition
  features
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️'):!item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="features=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="features" ${item.getName==features?'checked':item.getName=='<h3><b>Body</b></h3>'||item.getName=='<h3><b>Piercing</b></h3>'||item.getName=='<h3><b>Tattoo</b></h3>'?'disabled':''} /><label>${item.getName=='Any features'||item.getName=='No features'||item.getName=='<h3><b>Body</b></h3>'||item.getName=='<h3><b>Piercing</b></h3>'||item.getName=='<h3><b>Tattoo</b></h3>'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any features
    No features
    <h3><b>Body</b></h3>
    Blemishes
      https://user.uploads.dev/file/bd4e9b553f4ffc6a1e9273e80d26e3dd.webp
      skin blemishes
      top=beauty mark on the face[age>=13?"{|, pimples|}":""]
      mid=beauty mark on the chest
      rear=beauty mark on the back
    Brown
      https://user.uploads.dev/file/018440c6b04a94a0535a1774389a8960.png
      mid=brown [chest]
      low=brown [holeReference]
      rear=[this.low]
    Freckles
      https://user.uploads.dev/file/a1839eee2ad3419398f79df1030030be.webp
      top=freckles on the face
      mid=freckles on the shoulders
      rear=[this.mid]
    Healthy blush
      https://user.uploads.dev/file/7e19e70141d48b7d538ed3f1f4124557.webp
      top=healthy blush
    Pink
      https://user.uploads.dev/file/06ac3316d3004261076099ee9000e756.png
      mid={light |}pink [chest]
      low={light |}pink [holeReference]
      rear=[this.low]
    Scars
      https://user.uploads.dev/file/c78addaff2d8eccfaf63882facce869b.webp
      top=scars on the face
      mid=scars on the body
      rear=scars on the back
    Tan
      https://user.uploads.dev/file/35521f42c8ce22a26cf13de58a163f2a.webp
    <h3><b>Piercing</b></h3>
    Ears
      https://user.uploads.dev/file/eea6767be050e17584381440f450eaff.webp
      top=ears piercing
      rear=[this.top]
    Lip
      https://user.uploads.dev/file/390310f5ecb690a5abb0d962eb99224a.webp
      top=lip piercing
    Navel♀️
      https://user.uploads.dev/file/beb4f3979d62d362219caf0097221b59.webp
      mid=eyebrow piercing
    Nipple♀️
      https://user.uploads.dev/file/2620a66bc989f85ca67471be58c59057.webp
      mid=nipple piercing
    Nose
      https://user.uploads.dev/file/c6f4a585d90528da4333e2099dee6503.webp
      top=nose piercing
    <h3><b>Tattoo</b></h3>
    Chest
      https://user.uploads.dev/file/88b240f8f3a7cf237c360a4e5704ba8a.webp
      mid=chest tattoo
    Dragon
      https://user.uploads.dev/file/80c57788406a1dd3dc5b212ad6b44f08.webp
      dragon tattoo
    Face
      https://user.uploads.dev/file/51c6149d99cb17729c12c9d3a8a7e704.webp
      top=face tattoo
    Flower
      https://user.uploads.dev/file/48385bdd9f25bafba13a54a0a9ce693a.webp
      flower tattoo
    Full body
      https://user.uploads.dev/file/f1d144e1658dcabe5ca8c0d68c5996b9.webp
      full body tattoo
    Neck
      https://user.uploads.dev/file/9a6ecb33632dedeed9ae81795e3d1843.webp
      top=neck tattoo
    Sleeve
      https://user.uploads.dev/file/0d007c8ccbd2284c3e969b666a03e829.webp
      mid=sleeve tattoo
      rear=[this.mid]
  makeup
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️'):!item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="makeup=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="makeup" ${item.getName==makeup?'checked':''} /><label>${item.getName=='Any makeup'||item.getName=='No makeup'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any makeup
    No makeup
    Dry
      https://user.uploads.dev/file/2ecb6e33089e5cf3ebabd455917a4832.webp
      no makeup
      dry and chapped lips
      dry and chapped skin
      dehydrated look
    Eyeliner
      https://user.uploads.dev/file/83ecf1dd962c7e9a12b8dc567e72a013.webp
      cat-eye flick
    Fake eyelashes♀️
      https://user.uploads.dev/file/cad2d700e644908f9612413588c5b1f7.webp
    Glam♀️
      https://user.uploads.dev/file/08276658d22dd0181d9415eea92d7883.webp
      lipstick and foundation
      eyeshadow and blush
      bronzer and concealer
      eyeliner and eyebrow pencil
    Goth
      https://user.uploads.dev/file/0f0b91e5b2d74f472ba65823fe7910ce.webp
    Heavy
      https://user.uploads.dev/file/300de9caaf994e1775b49d48d456a42a.webp
      heavy eyeliner, heavy eyeshadow
      heavy blush, heavy bronzer, heavy concealer
      heavy foundation, bright lipstick
      heavy mascara and setting
      fake eyelashes, lip contouring
    Joker♂️
      https://user.uploads.dev/file/c90d8ed31366677a2db2a1249309fa4b.webp
      white face
      red lips and nose
      red cheeks and eyebrows
      red eyeliner and eyeshadow
      red blush and bronzer
      red concealer and foundation
    Lip contouring♀️
      https://user.uploads.dev/file/bb62b6c55c9653b82b6e44cd597f16d0.webp
    Lipstick♀️
      https://user.uploads.dev/file/00e36259d076b7e802c35bf04151dbb2.webp
      very light makeup
    Natural
      https://user.uploads.dev/file/91728e5ebcaca8bdeb3453ab28c5f080.webp
    Punk
      https://user.uploads.dev/file/59e4a376fa1c00aa538392b9134bf364.webp
    Rock
      https://user.uploads.dev/file/c069d22caf3f305099884e7b291068f3.webp
      dark eyeshadow and eyeliner
      dark eyebrow pencil
    Smokey♀️
      https://user.uploads.dev/file/f96ddd3dc96595344fed40ca8bdf8f58.webp
    Tribal
      https://user.uploads.dev/file/f66d77d6c4943ded6c0dc513aa523e0a.webp
      [tribal] face paint
      [!covered.includes("mid")?tribal+" body paint":""]
  condition
    $output = [this.selectAll.filter(item => !gender.includes('♂️') ? !item.getName.includes('♂️'):!item.getName.includes('♀️')).map(item => `<div><input value="${item.getName}" onchange="condition=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="condition" ${item.getName==condition?'checked':item.getName=='<h3><b>General</b></h3>'||item.getName=='<h3><b>Fight</b></h3>'||item.getName=='<h3><b>Explicit</b></h3>'?'disabled':''} /><label>${item.getName=='Any condition'||item.getName=='<h3><b>General</b></h3>'||item.getName=='<h3><b>Fight</b></h3>'||item.getName=='<h3><b>Explicit</b></h3>'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any condition
    <h3><b>General</b></h3>
    Cold
      https://user.uploads.dev/file/cd5b278350173435f5a4ed3b210dd0f9.webp
      shivering from the cold weather{, icicles hanging from the [actorReference.subject]'s [hairLength=="Bald♂️"?"head":"hair"] and [sceneNude?"body":"clothing"]|, hot air coming out of the [actorReference.subject]'s mouth and nose as mist and becomes frost on the chin and [!sceneNude?"clothing":"shoulders"]|}
    Dirty
      https://user.uploads.dev/file/2f52f01fbd2d64fff4fcae4ea3bde35c.webp
    Hot
      https://user.uploads.dev/file/bf2ee065f0bb2c0292a9b5c1ab1126ba.webp
      sweating from the hot weather, the face is flushed
    Wet
      https://user.uploads.dev/file/a2b174acd763bfc49db9d4ef1ae91395.webp
    Wet hair
      https://user.uploads.dev/file/4706771b8766f9dd8d3f6574b91aa439.webp
    <h3><b>Fight</b></h3>
    Bloodied
      https://user.uploads.dev/file/bc4f0d0245e14cbd1bf46c12a9d8e440.webp
    Bruised
      https://user.uploads.dev/file/dcf7e3dead5a015226a46b85fa9148a6.webp
    Swallen eye
      https://user.uploads.dev/file/827b70e6e04e6243bbfe3109caa1e5bd.webp
      swallen eye, bruised and battered, indicating [actorReference.subject] has been in a physical altercation
      {right|left} eye is swollen shut with a dark purple and black bruise and the other eye is slightly bloodshot
    <h3><b>Explicit</b></h3>
    Abused♀️
      https://user.uploads.dev/file/c2a1194f31885d321e118bc24ab96ee5.webp
      hand prints from slapping, sweating
      [featuresList.condition["Being stripped♀️"].selectAll.filter((item,index) => `${index == 0 ? '': item}`).joinItems(", ")]
      [sceneNude?"":" the clothing is ripped in several places"]
      [hairLength=="Bald♂️"||/low/i.test(camera)?"":"hair in disarray"]
      [!cameraAngles.includes("top")?"":"teary eyes"+[/no makeup|dry/i.test(makeup)?"":", running eyeliner"]]
      [camera=="top"||/oral|job/i.test(pose)||thingType!=1?"":[age<18?featuresList.condition["Deflorated♀️"].selectAll.filter((item,index) => `${index==0?'':item}`).joinItems(", "):""]]
      [thingType!=1?"":featuresList.condition["Came on"].selectAll.filter((item,index) => `${index == 0 ? '': item}`).joinItems(", ")]
    Being stripped♀️
      https://user.uploads.dev/file/2221cbca6589cbf6fbb89b7bd7fd2897.webp
      [sceneNude?"":"being stripped by the [POV]'s hands"]
    Came on
      https://user.uploads.dev/file/be878ed7a407bc8150c5e176d8eee2d5.webp
      sticky white translucent liquid [camera!="rear"&&camera!="top-mid-low"?"covers the [actorReference.subject]'s "+view.lowerCase:sceneSex?[/job/i.test(pose)?"covers ":"inside "]+"the [actorReference.subject]'s [hole]":"covers the [actorReference.subject]"]
      and [sceneWeightless?"floating around in bubbles":sceneWet?"being washed away":"dripping down"]
    Deflorated♀️
      https://user.uploads.dev/file/7080f38c6b765b49b74057ca0d96e1af.webp
      deflorated
      broken hymen
      small amount of blood is dripping from the [thing] and the [actorReference.subject]'s [holeReference]
      and [sceneWeightless?"floating around in bubbles":sceneWet?"being washed away":"dripping down"]
    Pregnant♀️
      https://user.uploads.dev/file/c47f5a133ccd6a4d6b7a34f44d8a0607.webp
 //<=Features
poseList // composition and perspective
  pose
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="pose=this.value;updatePoseControls();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="pose" ${item.getName==pose?'checked':item.getName=='<h3><b>Solo</b></h3>'||item.getName=='<h3><b>Interactive</b></h3>'||item.getName=='<h3><b>Explicit</b></h3>'?'disabled':''} /><label>${item.getName=='Any pose'||item.getName=='<h3><b>Solo</b></h3>'||item.getName=='<h3><b>Interactive</b></h3>'||item.getName=='<h3><b>Explicit</b></h3>'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any pose
    <h3><b>Solo</b></h3>
    Arms behind
      https://user.uploads.dev/file/085e4d1509fb51528ee429b5b3bcb50d.webp
      standing[/edge|seat/i.test(sceneDimensions)?" with one knee":/against/i.test(sceneDimensions)?" and leaning":""][sceneDimensions][actorType=="humanoid"?" with arms behind the back":""]
    Arms crossed
      https://user.uploads.dev/file/9bf0f9e17b672a9b38c68ad73d952dc9.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?"arms crossed on the {chest|waist|stomach}":""]
    Bending
      https://user.uploads.dev/file/4556ca47b38db139d7ca1ac6201ebe78.webp
      bending forward[actorType=="humanoid"&&/against|edge|seat/i.test(sceneDimensions)?" with the elbows":""][sceneDimensions]
    Bowing
      https://user.uploads.dev/file/7ff70614e02be7237bae68cc9a106a26.webp
      showing respect by bowing, bent on the waist, head bowed, arms straight to the sides[sceneDimensions]
    Clapping
      https://user.uploads.dev/file/0d4c3d04bd00e778094acb05b2df81e9.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?"clapping":"aproving"]
    Climbing
      https://user.uploads.dev/file/44754723cf6c9311667b5408713c079e.webp
      climbing [sceneSuspendable||/boxing ring/i.test(scene)?"up on the "+scene.lowerCase:/bench|couch|fence|sofa|wall/i.test(scene)?"over the "+scene.lowerCase:/bath|hot tub|jacuzzi|pool|window/i.test(scene)||sceneTransportation?"into the "+scene.lowerCase:"up a {metal|wooden} step ladder"]
    Crawling
      https://user.uploads.dev/file/3a44d0d18e9fe9b86d44de5d6cbe881c.webp
      [actorType=="humanoid"?"crawling on the stomach with one leg to the side, one arm forward":"crawling"][sceneDimensions] {towards|away from|past} the camera
    Crouching
      https://user.uploads.dev/file/6268c3145dc8782974673813a91619c4.webp
      crouching[actorType=="humanoid"?[/edge|seat/i.test(sceneDimensions)?" with the hands":""]:""][sceneDimensions]
    Cute
      https://user.uploads.dev/file/d0536785be45fce671f588340a2fed55.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing{ with one ankle up and to the side|}"][sceneDimensions]
      [actorType=="humanoid"?"doing a cute pose with the head tilted to the {right |left |}side and the hands {on the {chest|waist|stomach}|doing a heart symbol}":"posing"]
    Dancing
      https://user.uploads.dev/file/a42bee6daf408a7b469e58078a8591cb.webp
      [actorType=="humanoid"?"doing "+[/pole/i.test(scene)?"pole":/candle/i.test(lighting)||/romantic|18/i.test(vibe)?"romantic":"{bachata|ballet|ballroom|belly|breakdance|chacha|energetic|flamenco|folk|hip-hop|jazz|jive|kizomba|merengue|paso doble|quickstep|rumba|samba|slow|swing|salsa|samba|tango|swing|waltz|zouk|zumba}"]+" dance moves"+[/edge|seat/i.test(sceneDimensions)?" with one knee":""]:"shaking"][sceneDimensions]
    Driving
      https://user.uploads.dev/file/8ebd79de8bdcbf58b29a98e8fd842b99.webp
      [actorType=="humanoid"?[sceneTransportation?"driving {a} "+scene.lowerCase:[sceneOpenAir?/medieval|renaissance|victor/i.test(vibe)?"driving {a} cart":"driving {a} {bus|car|motocycle|scooter|tractor|truck}":"sitting"]+sceneDimensions]:"sitting[sceneDimensions]"]
    Eating
      https://user.uploads.dev/file/b14ae0c5ab6c0e8ce96e9e7316dda4f4.webp
      [food="{sandwich|burger|pizza|hotdog|pasta|sushi|salad|fruit|ice cream|cupcake|donut|chocolate|popcorn|chips|fries|ramen|curry|rice|noodles|soup|stew|roast|grill|bbq|meat|fish|seafood|vegetables|dessert|pastry|cake|pie|tart|pudding|yogurt|cheese|bread}".evaluateItem,""]
      eating[actorType=="humanoid"?" [food]{, chewing|, mouthful|}"+[/edge|seat/i.test(sceneDimensions)?", the [food] is":", holding the [food] in hands"]:""][sceneDimensions]
      focused on the food
    Fixing the hair
      https://user.uploads.dev/file/68895dce9c7ee834d93accb4be9e10d7.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":"standing"][actorType=="humanoid"?" with the head tilted to the {right |left |}side, and gently fixing the hair":""][sceneDimensions]
    Floating
      https://user.uploads.dev/file/9b925bbb2bf84b0f26cc324e0ed246a1.webp
      [sceneWeightless||sceneWet?"floating":"stationary"][sceneDimensions]
    Flying
      https://user.uploads.dev/file/645d1cf8ed1a1e846cb5885bccb7a532.webp
      [sceneWeightless||/alien|angel|bird|demon|fairy/i.test(actor)?"flying {above|away from|past|towards} the camera":"jumping"][sceneDimensions]
    Go away! gesture
      https://user.uploads.dev/file/1578bef52ee013ed3426004dc5b31ce7.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?"rudely sticking the palm forward telling the viewer to go away while looking sideways":"looking sideways, disinterested in the viewer"]
    Hands up
      https://user.uploads.dev/file/5cdc624ac549fb396c0d0068a0458589.webp
      standing[actorType=="humanoid"?[/edge|seat|against/i.test(sceneDimensions)?" and leaning":""]+sceneDimensions+", with the arms up in the air and hands resting on the top of the head":sceneDimensions]
    Hands on hips
      https://user.uploads.dev/file/ee49316f93c202ed0becd707c72a027d.webp
      standing[actorType=="humanoid"?[/edge|seat|against/i.test(sceneDimensions)?" and leaning":""]+sceneDimensions+", with hands on the hips":sceneDimensions]
    Hands on knees
      https://user.uploads.dev/file/eef67bfd5af971ccc9281e014dac01a8.webp
      sitting[actorType=="humanoid"?" with hands on the knees":""][sceneDimensions]
    Hanging
      https://user.uploads.dev/file/23a1c416d847570a4d8dd1c78e4aa309.webp
      [sceneSuspendable?"hanging{| upside down| {right|left} side up| sideways|}":actor=="humanoid"?"on tiptoes":"standing"][sceneDimensions]
    Heroic
      https://user.uploads.dev/file/f6e28c22f366578bbd89888f5c781f82.webp
      [actorType=="humanoid"?"doing {superhero pose after saving the world|{hands on hips|arms crossed|fist raised high victoriously} hero pose}":"posing"][sceneDimensions]
    High kick
      https://user.uploads.dev/file/16cb7d148f77e01c12950a2555b36f61.webp
      [actorType=="humanoid"?/merm/i.test(actor)?"striking with the tail high":"performing a high side kick in a martial arts stance, torso is twisted to face the direction of the raised leg"+[/edge|seat|against/i.test(sceneDimensions)?" while supporting with one hand":""]:"striking"][sceneDimensions]
    Jumping
      https://user.uploads.dev/file/eaf177a1bafd36f26524605013ea769f.webp
      jumping {towards|away from|past} the camera[sceneDimensions]
    Kneeling
      https://user.uploads.dev/file/62ceac875ada2d2f6aa042ff2046865e.webp
      kneeling[view=="POV"?" in front of the [POV]":" down"][sceneDimensions]
    Levitating
      https://user.uploads.dev/file/5095c94413f6e66aaf4a6c1217bcf8f7.webp
      levitating in the air[actorType=="humanoid"?[camera=="top"?"":" in a yoga pose with legs crossed"]:""][sceneDimensions]
    No! gesture
      https://user.uploads.dev/file/5bf0c7130cd52254edf7c2cf0bedd446.webp
      forming a denying cross with the [actorReference.subject]'s forearms over the chest, indicating strong disagreement
      the head is turned sideways, not looking at the viewer
    On all fours
      https://user.uploads.dev/file/1f81a1c35c9afdcbb65c13e009239c8c.webp
      [actorType=="humanoid"?"on all fours with the back arched"+[/edge|seat/i.test(sceneDimensions)?" and with the elbows":""]:"sitting"][sceneDimensions]
    On the back
      https://user.uploads.dev/file/ed26d369d9c912a53a30de53ffdda406.webp
      lying[actorType=="humanoid"?" relaxed on the back":""][sceneDimensions]
    On the side
      https://user.uploads.dev/file/1183366117a3f464462f9047a23c34fe.webp
      lying[actorType=="humanoid"?" relaxed on the side":""][sceneDimensions]
      [actorType=="humanoid"?"knees bent, hand propping the head":""]
    On the stomach
      https://user.uploads.dev/file/bb1f66ceded91fd855a1cf270d3e0076.webp
      lying[actorType=="humanoid"?" relaxed on the stomach{ head forward| with the back to the [POV]|}":""][sceneDimensions]
    On tiptoes
      https://user.uploads.dev/file/a10f6bde01311199dfe08143712b34e2.webp
      standing[actorType=="humanoid"?" on tiptoes and reaching up with the hands":""][sceneDimensions]
    Pointing gesture
      https://user.uploads.dev/file/ac27646955a12519a93690262914c20e.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?[/edge|seat/i.test(sceneDimensions)?"politely pointing with the both hands"+sceneDimensions:"pointing with the index finger of the {left|right} hand"]:""]
    Posing
      https://user.uploads.dev/file/b47f4b35e7258cf7b2f9fe1703c575de.webp
      [actorType=="humanoid"?"doing {high fashion event|professional model|beauty contest body showing off|one hand on the hip wide stance|arms outstretched to the sides, forming a T-shape, asking for applause|showing off} pose":"posing"][sceneDimensions]
    Praying
      https://user.uploads.dev/file/809d772c6a84a8a19bc08b6dfe7fa747.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"{standing|kneeling down}"][sceneDimensions]
      [actorType=="humanoid"?"praying":""]
    Propping head
      https://user.uploads.dev/file/a6e90c62499bf4d19fb497ebc3613f8f.webp
      sitting[actorType=="humanoid"?[/edge|seat/i.test(sceneDimensions)?" with one elbow":""]:""][sceneDimensions] [actorType=="humanoid"?" and the head propped on the hand":" in a balanced position"]
    Punching
      https://user.uploads.dev/file/4cbbb8a2abcf8df5a2c25b2648d5be8e.webp
      leaping[actorType=="humanoid"?" and performing a punch":""] {towards|away from|past|to the side of} the camera[sceneDimensions]
    Reading
      https://user.uploads.dev/file/7f3f082a38bf20564384c6681d445594.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?"reading, holding a book, looking at the book":"concentrated"]
    Riding
      https://user.uploads.dev/file/1143154b5a3f5380fb3332e40849cff5.webp
      [actorType=="humanoid"?[/cycle|horse|scooter/i.test(scene)?"riding {a} "+scene.lowerCase:sceneOpenAir?"riding {a} {bike|horse|motocycle|quadracycle}":"sitting"+sceneDimensions]:"sitting"+sceneDimensions]
    Running
      https://user.uploads.dev/file/7a8ee8b2286bf7537e277733fb386927.webp
      running {towards|away from|past} the camera[/edge|seat|against/i.test(sceneDimensions)?" and drifting with one hand":""][sceneDimensions]
    Shush!
      https://user.uploads.dev/file/576c3c974e84c4c3d2fe4196ee19a73d.webp
      shushing, saying the viewer to keep silent, by placing the index finger of the {left|right} hand in front of the perking mouth
    Sitting
      https://user.uploads.dev/file/490faf1ae741579f27c89ec250f191a6.webp
      sitting[/against/i.test(sceneDimensions)?" and leaning with the back":""][sceneDimensions]
    Sleeping
      https://user.uploads.dev/file/fc327a8c62c07abe946db914846b0df2.webp
      [actorType=="humanoid"||actorType=="animal"?"lying down relaxed and sleeping, eyes closed":"lying down"][sceneDimensions]
    Squatting
      https://user.uploads.dev/file/fecbccebf51c65977343d956bf4a1536.webp
      [/merm/i.test(actor)?"lying":"squatting"][sceneDimensions]
    Standing
      https://user.uploads.dev/file/4a0b55d0d50f7797bc8e82720092d0c4.webp
      [mood=="Drunk"&&actorType=="humanoid"?"having trouble standing, drunk pose":"standing"][/edge|seat|against/i.test(sceneDimensions)?" and leaning":""][sceneDimensions]
    Swimming
      https://user.uploads.dev/file/f00e5823db90f2c1e1f2cab7a61b437a.webp
      [sceneWet?"floating"+[sceneSpace?" in space":" in the water"]+" with one hand up and forward and body horizontally stretched out and swimming":"crawling on stomach {towards|away from|past} the camera"+[/edge|seat|against/i.test(sceneDimensions)?" with one hand":""]][sceneDimensions]
    Turned Around
      https://user.uploads.dev/file/79780b40135a5c387bf852ce5d0d1305.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      turned around looking back over the shoulder at the camera
    Typing
      https://user.uploads.dev/file/0354c5bdca24ab7c11190535c91f8cf6.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?"typing"+[accessories=="Laptop"?" on the laptop":accessories=="Smartphone"?" on the smartphone":""]+", looking at the {screen|keyboard}":"concentrated"]
      focused
    Walking
      https://user.uploads.dev/file/7cecf7ec329124585236242e2dfb245c.webp
      [mood=="Drunk"&&actorType=="humanoid"?"having trouble walking, drunk walk":"walking {away from|towards|past} the camera"][/edge|seat|against/i.test(sceneDimensions)?" with one hand":""][sceneDimensions]
    Waving
      https://user.uploads.dev/file/b514515e5e56043d5908d3dc90085c5d.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?"waving {a hand|both hands}"+[chaNum==1?" towards the camera":""]:"acknowledging the presence"]
    Working
      https://user.uploads.dev/file/d1a5b3595724e664ed890446f5321aa7.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?"working":"looking busy"]
      focused
      concentrated
    Writing
      https://user.uploads.dev/file/6333bbd2b8f01b3a446818a78472c408.webp
      sitting[scene=="Any scene"?" at a desk":/edge/i.test(sceneDimensions)?" on a chair with elbows":/against/i.test(sceneDimensions)?" and leaning with the back":""][sceneDimensions]
      [actorType=="humanoid"?"writing, holding a pen, looking at the paper":""]
      focused
    Yoga
      https://user.uploads.dev/file/26236ec9f32846cd8fff3edc937f196d.webp
      [actorType=="humanoid"?"doing a yoga pose":""][sceneDimensions]
    <h3><b>Interactive</b></h3>
    Holding hands
      https://user.uploads.dev/file/ae13d1d36bcd4458942c49451b790ed6.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?"holding hands"+[charNum==1?" with the [POV]":""]:"leaning close"]
    Hugging
      https://user.uploads.dev/file/b86b74529ed42b636392fd1042a4ac20.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"standing and leaning":"standing"][sceneDimensions]
      [actorType=="humanoid"?[charNum==1?"spreading arms invitingly apart ready for a hug":"tenderly hugging"]:"leaning close"]
    Massage back
      https://user.uploads.dev/file/7f64eb5af509372af74c6b87d0ac05ce.webp
      [actorType=="humanoid"?"lying on the stomach with the back to the [POV]":"lying down"][sceneDimensions]
      [actorType=="humanoid"?"getting a back massage from the [POV]'s hands":""]
    Massage foot
      https://user.uploads.dev/file/23b481fbbc870ea6e17d3aacd6c4a982.webp
      sitting[/against/i.test(sceneDimensions)?" and leaning with the back":""][sceneDimensions]
      [lowerBodyPart=[/merm/i.test(actor)?"tail":/minotaur/i.test(actor)?"hoof":"foot"],""]
      [actorType=="humanoid"?"{getting a [lowerBodyPart] massage from the [POV]'s hands|doing a [lowerBodyPart] massage to the [POV]}":""]
    On the lap
      https://user.uploads.dev/file/111.webp
      sitting on the [POV]'s lap[sceneDimensions]
      [actorType=="humanoid"&&age>=18?"taking highly erotic poses":""]
    <h3><b>Explicit</b></h3>
    Bending sex
      https://user.uploads.dev/file/29354e4556ae3bacb02dd7258fe495e5.webp
      bending forward[actorType=="humanoid"?" on the waist, pelvis back pressed against the [POV], and with the "+[/against|edge|seat/i.test(sceneDimensions)?"elbows":"hands on the knees"]:""][sceneDimensions]
    Cowgirl sex
      https://user.uploads.dev/file/4a506ce093c786b966d74dfe3ad3650f.webp
      squatting[actorType=="humanoid"?" on top of the [POV]":""][sceneDimensions]
    Doggy sex
      https://user.uploads.dev/file/99f841649c261f059377fe0d21cb6719.webp
      on all fours[actorType=="humanoid"?" with the back to the [POV]"+[/on/i.test(sceneDimensions)?" and with the elbows":""]:""][sceneDimensions]
    Flashing
      https://user.uploads.dev/file/5885b7140b71f859549aa3dabc014d9d.webp
      [position="{standing|sitting|lying|turned around|on all fours}".evaluateItem,""]
      [stripItem=[position=="turned around"?"bottom":["{top|bottom}".evaluateItem]],""]
      [position+[/edge|seat/i.test(sceneDimensions)?[position=="standing"||position=="turned around"?" and leaning":position=="on all fours"?" with one elbow":""]:""]+[sceneDimensions]+[position=="on all fours"?[stripItem=="bottom"?" with the back to the [POV]":" with the [chest] towards the [POV]"]:""]]
      [actorType=="humanoid"?"showing off "+[stripItem=="top"?"the [chest]":"the [holeReference][plural]"]+" right in the camera":""]
    Footjob
      https://user.uploads.dev/file/2308e38ee9728d96ddeb81ed4664fa83.webp
      sitting[actorType=="humanoid"?" in front of the [POV]":""][/against/i.test(sceneDimensions)?" and leaning with the back":""][sceneDimensions]
    Handjob
      https://user.uploads.dev/file/cf67f8a3e37ef6ba0ddd0050c5586577.webp
      [/edge|seat/i.test(sceneDimensions)?"sitting":/against/i.test(sceneDimensions)?"sitting and leaning with the back":"squating"][actorType=="humanoid"?" in front of the [POV]":""][sceneDimensions]
    Legs up sex
      https://user.uploads.dev/file/520493bb7c20bbbc46d3201d4c6c18ee.webp
      lying relaxed on the back[sceneDimensions][actorType=="humanoid"?", with the legs high up{ and spread apart| and pressed together| and turned to the {left|right} side}, and the [hole] turned towards the [POV]":""]
    Lying on the side sex
      https://user.uploads.dev/file/975ed802cfcf0320c33f29045f20195d.webp
      lying relaxed on the side[sceneDimensions][actorType=="humanoid"?", with knees bent to the chest and the [hole] turned towards the [POV]":""]
    Lying on the side oral
      https://user.uploads.dev/file/6bcf432239908321a29c68a27d256b3e.webp
      lying on the side[sceneDimensions][actorType=="humanoid"?", with head horizontally on the sitting [POV]'s lap":""]
    Missionary sex
      https://user.uploads.dev/file/89beb371eee6e1ba520cd0c83cdb7357.webp
      lying relaxed on the back[sceneDimensions][actorType=="humanoid"?" in front of the [POV]":""]
    Oral
      https://user.uploads.dev/file/6f8ce61c9d836baec59b76896ed5f6f0.webp
      [/fair/i.test(actor)?"hugging the [thing] with the arms and legs climbing to the top of it":[position="{on all fours|kneeling|squating|sitting}".evaluateItem]][/edge|seat/i.test(sceneDimensions)&&/standing/i.test(position)?" and leaning":""][sceneDimensions][actorType=="humanoid"?" with the [hole] down in front of the [thing]":""]
    Reaching down oral
      https://user.uploads.dev/file/8db7b9f7f60e43ca9496292f1a3fa6c2.webp
      lying on the stomach[actorType=="humanoid"?/edge|seat|against/i.test(sceneDimensions)?" with the legs up "+sceneDimensions+" and the arms reaching down to the floor, head down, reaching down off the edge to the [POV] sitting much lower underneath":" with the head down and towards the [POV]'s groin"+sceneDimensions:sceneDimensions]
    Reversed cowgirl sex
      https://user.uploads.dev/file/7ac3e5c4ac71b2858e2ddd22112cd52c.webp
      squatting[actorType=="humanoid"?" on top and with the back to the [POV]"+[/edge|seat|against/i.test(sceneDimensions)?" with the arms":""]:""][sceneDimensions]
    Reversed missionary sex
      https://user.uploads.dev/file/e0ac91c18f7082538983393428e297e1.webp
      lying relaxed on the stomach[actorType=="humanoid"?" with the back to the [POV]":""][sceneDimensions]
    Reversed sitting sex
      https://user.uploads.dev/file/b27084b960dd14469c7deb6247d0c939.webp
      sitting[actorType=="humanoid"?" with the back on the [POV]'s lap"+[/edge|seat|against/i.test(sceneDimensions)?" with the arms":""]:""][sceneDimensions]
    Reversed standing sex
      https://user.uploads.dev/file/051ecac9bfd0d36f2ded29cc88420c77.webp
      standing[actorType=="humanoid"?" with the back to the [POV]"+[/edge|seat|against/i.test(sceneDimensions)?" and leaning with the arms":""]:""][sceneDimensions]
    Sex
      https://user.uploads.dev/file/e1a0af36910d6441aa092c95cfff7501.webp
      sex()=>
        let sentence=[], her="the [actorReference.subjectSingular]'s", she="the [actorReference.subjectSingular]"; 
        sentence.push(she+" is ");
        if (/legs|missionary|top-down/i.test(pose)||/missionary|top-down/i.test(position)){
          sentence.push("underneath ");
        }else if (/cowgirl|sitting/i.test(pose)){
          sentence.push("on top of ");
        }else if (/bending|doggy|revers/i.test(pose)){
          sentence.push("facing away from ");
        }else if (/on the side oral/i.test(pose)||position=="Lying on the side oral"){
          sentence.push("with the head on the lap of ");
        }else if (/side/i.test(pose)||position=="Lying on the side sex"){
          sentence.push("turned to the side of ");
        }else{ sentence.push("directly in front of ");}
        sentence.push("the [POV]");
        if (/job/i.test(pose)||holeType==2){
          sentence.push(her+" [hole] "+[/feet|tits/i.test(hole)?"are":"is"]+" wrapped around the [thing]");
        }else if (/top-down/i.test(pose)||position=="Top-down oral"){
          sentence.push("the [thing] is angled down inside the [actorReference.subjectSingular]'s [hole] to the base, as deep as the back of the throat");
        }else{sentence.push("the [thing] is inside of "+her+" [hole]");}
        if (thingType==3){
          sentence.push(she+" is getting dildoed by the [POV]");
        }else if (thingType==4){
          sentence.push(she+" is getting fingered by the [POV]");
        }else if (/top-down/i.test(pose)||position=="Top-down oral"){
          sentence.push(her+" [hole] is being used for rough oral coitus by the [thing]");
        }else if (/sleep/i.test(pose)){
          sentence.push(her+" [hole] is being used for pleasure by the [thing]");
        }else if (/job|oral/i.test(pose)&&age<=17){
          sentence.push(she+" is stroking the [thing] with the [hole]");
        }else{
          if (/job|oral/i.test(pose)){
          sentence.push(she+" is giving ");
          }else{sentence.push(she+" is having ");}
          if (/sex/i.test(pose)){
            if (/merm/i.test(actor)){sentence.push("oral ");
            }else {sentence.push("[holeReference] ");}
          }
          sentence.push([age>=18?pose.lowerCase:pose.lowerCase.replace(/sex/,"intercourse")]+" ");
          sentence.push([(/job|oral/i.test(pose))?"to":"with"]+" ");
          sentence.push("the [POV]")
        }
        sentence.push(she+" is held by the [POV]'s hands on the ");
        if (/top-down/i.test(pose)||position=="Top-down oral"){
          sentence.push(" head firmly like it's a toy for pleasure");
          if (!/sleep/i.test(pose)){sentence.push("the [actorReference.subjectSingular]'s eyes are slightly teary from the [thing] deep inside [actorReference.pronounPossessive] throat");}
        }else if (hole=="mouth"){
          sentence.push("{side|back|top} of the head".evaluateItem);
          sentence.push("{saliva dripping from the chin|eyes slightly teary from gagging on the [thing] deep inside the throat|}".evaluateItem);
        }else if (/legs/i.test(pose)){
          sentence.push("legs");
        }else if (/doggy|revers/i.test(pose)){
          sentence.push("{hips|arms}".evaluateItem);
        }else if (/job/i.test(pose)){
          sentence.push(holeReference);
        }else {
          sentence.push("{hips|waist|thighs}".evaluateItem);
        }
        if (charNum>1){
          sentence.push("and the other ");
          if (charNum==2){sentence.push(she+" is ");
          }else{sentence.push("[actorReference.subject] are ");}
          sentence.push("propping the [actorReference.subject] up")
        }
        return combine(sentence);
      [this.sex()]
    Sitting sex
      https://user.uploads.dev/file/6fa0ce4084dc9f1fd2d98afbd186fa58.webp
      sitting[actorType=="humanoid"?[/edge|seat/i.test(sceneDimensions)?"":" on the [POV]'s lap"]:""][sceneDimensions]
    Sleeping sex
      https://user.uploads.dev/file/658961951470dc88003ad222cca54155.webp
      sleeping
      [position="{Lying on the side sex|{Reversed m|M}issionary sex}".evaluateItem,""]
      [poseList.pose[position].selectAll.filter((item,index) => `${index==0?'':item}`).joinItems(", ")]
    Sleeping oral
      https://user.uploads.dev/file/13f4c510feca88a005d879f986cc5bff.webp
      sleeping
      [position="{Lying on the side oral|Top-down oral}".evaluateItem,""]
      [poseList.pose[position].selectAll.filter((item,index) => `${index==0?'':item}`).joinItems(", ")]
    Standing sex
      https://user.uploads.dev/file/59261cf27d90dea9adf7247759c3da8b.webp
      standing[actorType=="humanoid"?" in front of the [POV]"+[/edge|seat|against/i.test(sceneDimensions)?" and leaning back with the arms":""]:""][sceneDimensions]
    Titjob
      https://user.uploads.dev/file/a6d9a85e481c02926f5491b2af0ec45a.webp
      kneeling[actorType=="humanoid"?" with the chest in front of the [thing]":""][sceneDimensions]
    Touching self
      https://user.uploads.dev/file/41b4e2c3e5537ad39d0ad24bdb297880.webp
      [position="{sitting|lying|standing|on all fours|turned around}".evaluateItem][/edge|seat|against/i.test(sceneDimensions)&&position=="standing"||position=="turned around"?" and leaning":""][sceneDimensions]
      [actorType=="humanoid"?"touching the {chest|glutes|[holeReference]} with one hand and sticking a "+[/dild/i.test(accessories)?[age>=18?accessories.lowerCase:[clothingList.Accessories[accessories].getLength>0?clothingList.Accessories[accessories].joinItems(", "):"finger"],""]:"finger"]+" inside the [holeReference] with the other giving self pleasure":""]
      [actorType=="humanoid"?"the head is tilted back and eyes half closed enjoying it":""]
    Top-down oral
      https://user.uploads.dev/file/333360e66e45a76985c2c5422bb88136.webp
      lying on the back with [actorReference.pronounPossessive] head[/edge|seat/i.test(sceneDimensions)||sceneSurface?"":" on the ground"][sceneDimensions]
      [actorType=="humanoid"?" the [actorReference.subjectSingular]'s head is arched back and [actorReference.pronounPossessive] [hole] opened":""]
  view
    $output = [this.selectAll.filter(item => actor=="Any actor"?item.getName.includes('🎞')||item.getName=="Any view":item).map(item => `<div><input value="${item.getName}" onchange="view=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="view" ${item.getName==view?'checked':''} /><label>${item.getName=='Any view'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any view
    Above
      https://user.uploads.dev/file/359b07ad3526a4a6fb908d647bf979c7.webp
      high-angle overhead shot looking down at the [actorReference.subject]
    Artistic🎞
      https://user.uploads.dev/file/2a2449cad8ce3d9af23cfa08e99e41c3.webp
      artistically tilted camera angle
    Back
      https://user.uploads.dev/file/652b40822e1c6bbc4b6c7b03fb48e654.webp
      close rear view focusing solely on the back capturing it from the shoulders to the lower back
    Behind
      https://user.uploads.dev/file/2d54a646a79909fea3be07f3abeb9386.webp
      rear view capturing the [actorReference.subject] from behind
    Below
      https://user.uploads.dev/file/965e213a2500bb532b02f865b09ebc3f.webp
      low-angle shot looking up at the [actorReference.subject] from a ground-level position
    Chest
      https://user.uploads.dev/file/ad76456b8f7f797c94662116b87468a6.webp
      [actorType=="humanoid"?"the{| side|} shot focuses solely on the [actorReference.subject]'s chest capturing it from the upper part to the beginning on the stomach":"upper part shot using 200mm lens"]
    Downblouse
      https://user.uploads.dev/file/3f673389d75f40a3d16d4cf3cafe5396.webp
      close candid shot[actorType=="humanoid"?", focusing solely on the [actorReference.subject]'s clevage":"of the upper part using 200mm lens"] from above downwards at a very steep angle
      the camera is positioned at an angle that captures as much of the the [actorReference.subject]'s clevage as possible peeking out from the neckline
      [actorType=="humanoid"?"the [actorReference.subject] is unaware of the camera, gazing into the distance and slightly leaning forward giving the camera a perfect view":""]
    Ears
      https://user.uploads.dev/file/f215c2cca3622ce0cf6c1b1f8ef720bc.webp
      [actorType=="humanoid"?"ear close-up using 200mm lens":"upper part shot using 200mm lens"]
    Eyes
      https://user.uploads.dev/file/decc11388679d54fe10d1301ac6f7233.webp
      [actorType=="humanoid"?"eye close-up using 200mm lens":"upper part shot using 200mm lens"]
    Face
      https://user.uploads.dev/file/0116acd5db40e9388834918ec627fce5.webp
      [actorType=="humanoid"?"face close-up using 50mm lens":"upper part shot using 50mm lens"]
    Feet
      https://user.uploads.dev/file/cae3de39791b6247116e9c7f8051f303.webp
      [actorType=="humanoid"?[/merm/i.test(actor)?"fish tail":/minotaur/i.test(actor)?"hoof":/demon/i.test(actor)?"cloven foot":"foot"]+" close-up using 200mm lens":"lower part shot using 200mm lens"]
    Front
      https://user.uploads.dev/file/d92ee4e509d944714c147f211d810b7a.webp
      straight-on perspective[actorType=="humanoid"?" providing a direct view of the [actorReference.subject] {knee|waist}-up":""]
    Full body
      https://user.uploads.dev/file/fb5b22df0cdfb64470cd144f93b38fdd.webp
      [actor=="Any actor"?"panorama":"full body shot capturing the [actorReference.subject] from head to toe"]
    Glutes
      https://user.uploads.dev/file/084cfdf54721e0d0d018b34687bc29d9.webp
      [actorType=="humanoid"?"close rear 200mm shot focusing solely on the [actorReference.subject]'s "+[sceneExplicit?[age>=18?'anus':'rear hole']:"coccyx"]+" capturing it from the upper to the lower part":[actor=="Any actor"?"panorama shot":"lower part shot using 200mm lens"]]
    GoPro🎞
      https://user.uploads.dev/file/c23e209c95eead099f8d1e7ff8583a09.webp
      GoPro action camera view
      [styleList.filter["fisheye"].selectAll.joinItems(", ")]
      [actorType=="humanoid"?"[actorReference.subject] is "+[sceneHandsFree?"holding":"wearing"]+" the camera on a long selfie stick, taking selfie":""]
    Hand
      https://user.uploads.dev/file/dc255b1ac945a29226bccfed4a30c318.webp
      [actorType=="humanoid"?"hand close-up using 200mm lens":"center of mass shot using 200mm lens"]
    Head
      https://user.uploads.dev/file/e7ba64fc77357ee32932d8e218dac1e1.webp
      [actorType=="humanoid"?"head {close-up|side profile} using 50mm lens":"upper part shot using 50mm lens"]
    Lips
      https://user.uploads.dev/file/5d02dfd823026a2762879cb3bf1b3d8b.webp
      [actorType=="humanoid"?"lip close-up using 200mm lens":"upper part shot using 200mm lens"]
    Lower body
      https://user.uploads.dev/file/5db6acdf5a4fa3215ac78b951994edbd.webp
      lower body shot capturing the [actorReference.subject] from the waist to the feet
    Multiview🎞
      https://user.uploads.dev/file/0e233ea1f4dea6ca0cab4e9850e2e4c8.webp
      collage featuring multiple views[actor=="Any actor"?" of the same place":" of the [actorReference.subject]"] in a single frame including [actorType=="humanoid"?"{side profile|face close-up|{full|upper|lower} body view|view from {above|below}|view from the {front|back}|{half turned|turned around looking back} view}".selectMany(3).joinItems(", "):" view from above and panorama"]
    Neck
      https://user.uploads.dev/file/6b449f005d8a1f9b3efb30ef7be84a5e.webp
      [actorType=="humanoid"?"neck close-up using 200mm lens":"upper part shot using 200mm lens"]
    Over-the-shoulder
      https://user.uploads.dev/file/6f6add98667808a0b11924e977a8aa80.webp
      over-the-shoulder shot[actorType=="humanoid"?", camera is placed above the back of the shoulder and the head of the [actorReference.subject] creating an immersive view of the scene from the [actorReference.subject]'s perspective. The the [actorReference.subject]'s {ear|head|shoulder} is partially visible in the {left|right} bottom corner of the frame, creating an over-the-shoulder composition":""]
    Panorama🎞
      https://user.uploads.dev/file/7720d2859450cf82ed4d7d8c79ac7d64.webp
      broad panorama perspective capturing a wide-angle view
      [styleList.filter["extended depth-of-field"].selectAll.joinItems(", ")]
    Portrait
      https://user.uploads.dev/file/9560c897da67b4f65636bf6b019d012e.webp
      portrait shot of the [actorReference.subject]
    POV🎞
      https://user.uploads.dev/file/a4d0b63935dde8243b37639c5d988120.webp
      interactive experience from the [POV]'s perspective
      [pose=="Any pose"||actor=="Any actor"?"the [POV]'s "+[/edge/i.test(sceneDimensions)?"elbow is resting"+sceneDimensions:/against|on/i.test(sceneDimensions)?"hand is resting relaxed"+sceneDimensions:"partially visible {hand|ear|forearm|shoulder} in the {left|right} corner of the frame"]:""]
    Side
      https://user.uploads.dev/file/2377368c6fc82355aad300fa080f57c0.webp
      side profile
    Stalker🎞
      https://user.uploads.dev/file/ddfce9c7edec26870f7e141d1aeb7eb3.webp
      [actor=="Any actor"?"":"the [actorReference.subject] [beVerb] unaware of the camera, turned away, gazing into the distance"]
      stalker experience from the [POV]'s perspective
      the view is tilted peeking from behind a [sceneOpenAir&&!/balcony|roof/i.test(scene)?"{bench|bush|car|corner|crowd of people|fence|trash bin|tree}".evaluateItem:sceneTransportation?"{a seat|handrails}".evaluateItem:"{corner|door|window}".evaluateItem] and obscured by the objects in the foreground, giving the sense of intense stealthy surveillance
      a part of the [POV]'s [sceneExplicit?"hand on the [thing]":"{hand holding a |}phone"] in a foreground corner is blurry[actor=="Any actor"?"":", shifting the attention to the subject of surveillance"]
      [styleList.filter["f/1.6 aperture"].selectAll.joinItems(", ")]
    Stomach
      https://user.uploads.dev/file/39e38be4b24f41de7d2ebc277224a7bc.webp
      [actorType=="humanoid"?"belly button close-up using 200mm lens":"center of mass shot using 200mm lens"]
    Thighs
      https://user.uploads.dev/file/db5107a695d9a0719b24b5c7dc13e3a9.webp
      [actorType=="humanoid"?"close 200mm shot focusing solely on the "+[/merm/i.test(actor)?"fish tail":sceneExplicit?holeReference:"thighs"]+" capturing it from the upper to the lower part":"lower part shot using 200mm lens"]
    Top-down🎞
      https://user.uploads.dev/file/9334d53089764b4c867c794c2cffc600.webp
      the high-angle [sceneOpenAir?"bird-eye":"ceiling"] camera capturing the [actor=="Any actor"?"scene":"[actorReference.subject]"] from a top-down perspective
    Upper body
      https://user.uploads.dev/file/dd560309c9ec18709316ba2ccd5c98a7.webp
      upper body shot capturing the [actorReference.subject] from the head to the waist
    Voyeur
      https://user.uploads.dev/file/c1927f0f33db585b6241e44f6728db23.webp
      close candid [actorType=="humanoid"?[clothingHasRim?[age>=18?"upskirt panty shot":"underpanties shot up the rim"]:"the lower [holeReference] shot"]:"shot"] from{ behind and|} below upwards
      the 200mm lens camera is positioned at a very low angle, almost touching the ground, looking upwards at a steep angle[actorType=="humanoid"?", focusing entirely on the "+[clothingHasRim?[age>=18?"":"under"]+"panties{ sticking to the "+"{[holeReference]^2|[holeRear]}|}":"[holeReference]"]+" capturing it from the upper to the lower part":""]
      [actorType=="humanoid"?"the [actorReference.subject] is unaware of the camera, gazing into the distance, while legs are fully open allowing the camera to capture the entire view":""]
  mood
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="mood=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="mood" ${item.getName==mood?'checked':''} /><label>${item.getName == 'Any expression'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any expression
    Angry
      https://user.uploads.dev/file/99f30cc46acef35640d68cea953ac78f.webp
      cheeks bulged with anger
      angry
    Annoyed
      https://user.uploads.dev/file/1e57aba0d05636c34fcb7524336be74c.webp
      annoyed
    Aroused
      https://user.uploads.dev/file/e0b34b991992ff63250386bdb0b71d8e.webp
      [age>=18?"aroused":"wanting a hug"]
    Ashamed
      https://user.uploads.dev/file/331f9ac03f40edb8f50fe6f9ef94bf50.webp
      looking {down|away}
      ashamed
    Calm
      https://user.uploads.dev/file/2dc7c47c46a3caf13a00cf574dca8161.webp
      neutral mood, calm
    Confused
      https://user.uploads.dev/file/8c86b18fd79093c08aaedc607e4e152c.webp
      confused
    Crying
      https://user.uploads.dev/file/af20dc74bb4ff6b4ca673abab0470801.webp
      crying
      sad
    Determined
      https://user.uploads.dev/file/8a3d2905942bc1553508ea549670ad10.webp
      slightly furrowed brow and a focused gaze with a hint of a defiant smirk
      the eyes are narrow and intense, suggesting concentration and resolve
      looking sideways
      serious and determined
    Disgusted
      https://user.uploads.dev/file/3b46b43d2eb011047349958e7d41430f.webp
      disgusted
    Drunk
      https://user.uploads.dev/file/9137c588c287885056683c4d681244c2.webp
      eyes unfocused
      head down
      drooling
      [age>=18?"drunk":"intoxicated"]
    Elated
      https://user.uploads.dev/file/74c68905d58e4115569a2c3a62f5a184.webp
      slightly smiling
      elated
    Enjoying
      https://user.uploads.dev/file/18067c8cfb49fa1d707353f65960b218.webp
      cheeks flushed
      enjoying it
    Enthusiastic
      https://user.uploads.dev/file/54236d226ea84552b10627ea30ca3bb7.webp
      enthusiastic
    Evil smile
      https://user.uploads.dev/file/bfca6c3375be2717605ec8f2f86be69d.webp
      sinister, menacing smile from under the brow
    Excited
      https://user.uploads.dev/file/ee5527b4edd6f773b4a9bdf7263605b5.webp
      emotional
      sweating
      excited
    Eyes closed
      https://user.uploads.dev/file/b1f60e8f71090eb229a1f35c9ec048b9.webp
      eyes closed
      peaceful
    Focused
      https://user.uploads.dev/file/6ec7625e56265cede0dca5d58846a178.webp
      concentrated
      focused
    Happy
      https://user.uploads.dev/file/9da70d39443dc42ceb66699e4cfd6391.webp
      content
      smiling
      laughing
      happy
    Hurt
      https://user.uploads.dev/file/11a9462ea5d9a8c386eea70026e18c21.webp
      grimacing in pain
      hurt
    Inocest Smile
      https://user.uploads.dev/file/8f1b1a1b8e1c1b1b1b1b1b1b1b1b1b1b.webp
      innocent smile
    Intimidating
      https://user.uploads.dev/file/4f3ceb048342b2b05d6fe507e357fba6.webp
      all angles and edges for facial features
      angry creases on the forehead
      angry creases around the eyes and the mouth
      intimidating
    Kissing
      https://user.uploads.dev/file/4a79fba041350b9f71ce1e09e453cd9d.webp
      eyes half closed
      [age>=18?[charNum==1?"sending air kisses to":"kissing"]:"head leaning forward, lips tenderly pressed"]
      perking the lips
    Looking sideways
      https://user.uploads.dev/file/51cd3db0594bbf433cf1b634d81cd380.webp
      head half turned
      looking sideways at the [POV]
      glaring
    Mad
      https://user.uploads.dev/file/55058ba5ffa436e02c5b821b3198829b.webp
      eyes wide open and looking in different directions
      drooling
      mad
    Outraged
      https://user.uploads.dev/file/0ddd3f8d7fff4f5b1ffe1e98b4e1f931.webp
      outraged
    Proud
      https://user.uploads.dev/file/e032caeaec7d3004d2d9356825fdc394.webp
      chin up
      proud
    Sad
      https://user.uploads.dev/file/144a9a6828ba4bd8311f16864e2263fe.webp
      sad
    Seductive
      https://user.uploads.dev/file/f01b54920afe292a45acb6fc3594ece6.webp
      one shoulder forward
      inviting gaze
      [age>=18?"flirting, seductive":"playful"]
    Shy 
      https://user.uploads.dev/file/0549771aa3103e4d40e2ccd4cc661bea.webp
      blushing
      looking {away|down}
      shy
    Singing
      https://user.uploads.dev/file/555ad6bd6b55f1da30ed308c37a8bc81.webp
      mouth {half|slightly|wide} open
      {|eyes{ half|} closed|}
      singing
    Submissive
      https://user.uploads.dev/file/bc5e63f372152c57ec650d98302ab38a.webp
      head bowed
      looking down
      [age>=18?"submissive":"shy"]
    Surprised
      https://user.uploads.dev/file/aebfd433e6552bce0b20821e079c4362.webp
      eyes wide open
      mouth slightly open
      startled
      surprised
    Talking camly
      https://user.uploads.dev/file/f4c92f36605a1ec4e499e97fea4a0813.webp
      mouth {slightly|half} open [view=="POV"?"while talking to the first person [POV]":"while talking"]
      {gesticulating|nodding|shaking head}
      talking
    Talking loudly
      https://user.uploads.dev/file/202268f9e2be1161d19548cb7c50f6f4.webp
      mouth {half|wide} open [view=="POV"?"while talking to the first person [POV]":"while talking"]
      energetically {gesticulating|nodding|shaking head|inquiring|demanding}
      talking
    Talking on the phone
      https://user.uploads.dev/file/321626a42f881fccdb49bff9720f36cf.webp
      talking on the phone
      [sceneHandsFree?"holding a phone to the ear, head tilted towards the phone":"a phone is lying near them"]
      mouth slightly open, talking
    Teasing
      https://user.uploads.dev/file/e4215f0768c1f14c43aae12168571e34.webp
      playful
      teasing
    Thoughtful
      https://user.uploads.dev/file/992829a018384c4d7e89850150ef4a26.webp
      thoughtful
    Tired
      https://user.uploads.dev/file/9df80fc94a07a37abc26f7a22eb10e5e.webp
      eyes half closed
      tired
    Tongue Out
      https://user.uploads.dev/file/6bd57f19184aefe3416b8ac910fe1d9c.webp
      mouth open
      tongue sticking out
      silly
    Worried
      https://user.uploads.dev/file/9388d494c9927c911b65d77913a6cd77.webp
      worried
    Yawning
      https://user.uploads.dev/file/ba442fa5b6f71046fc754054a6ca772c.webp
      covering mouth with a {palm|fist} while yawning
      yawning
    Yelling
      https://user.uploads.dev/file/ce4afdddfe7f2d50429ded79e78521aa.webp
      yelling
sceneList // place, lighting, weather, vibe
  scene
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="scene=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="scene" ${item.getName==scene?'checked':item.getName=='<h3><b>Inside</b></h3>'||item.getName=='<h3><b>Outside</b></h3>'||item.getName=='<h3><b>Places</b></h3>'||item.getName=='<h3><b>Transportation</b></h3>'||item.getName=='<h3><b>Highlights</b></h3>'||item.getName=='<h3><b>Space</b></h3>'?'disabled':''} /><label>${item.getName=='Any scene'||item.getName=='Blank'||item.getName=='<h3><b>Inside</b></h3>'||item.getName=='<h3><b>Outside</b></h3>'||item.getName=='<h3><b>Places</b></h3>'||item.getName=='<h3><b>Transportation</b></h3>'||item.getName=='<h3><b>Highlights</b></h3>'||item.getName=='<h3><b>Space</b></h3>'?'':'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any scene
    Blank
    <h3><b>Inside</b></h3>
    Armchair
      https://user.uploads.dev/file/7ac6502c0a1c993a93a964cc73c9347a.webp
      modern, cozy living room featuring {an armchair|two patterned armchairs facing each other} with {a} {dark wooden coffee table in the center|tv screen on the wall|floor lamp in the corner|rug on the floor|wooden shelving unit with books|modern art on the wall}
    Attic
      https://user.uploads.dev/file/3a2ba5b56dd9d79ec0bbeb64e6ce5288.webp
      rustic attic bedroom with a triangular wooden ceiling and exposed beams
      the room features light-colored, weathered wooden walls and a matching wooden floor
      at the small window, there's {a} {amateur telescope|wooden chair|simple bed}
    Basement
      https://user.uploads.dev/file/ba5b13f7ef7eec673f5e35771275a399.webp
      cluttered, partially renovated basement with a rough, unfinished appearance
      the floor is covered in cement dust and cardboard box pieces, and the walls are made of exposed, weathered stone
      the ceiling is partially visible, showing exposed wooden beams and insulation
      a ladder leaning against the back wall, a plastic bin, a plastic tub prepared for concrete mixing
    Bathroom
      https://user.uploads.dev/file/80dbc7c9efbcd628daf6ef277ea603d7.webp
      small, tidy bathroom with a marble-tiled floor
      countertop, white oval sink, and chrome faucet, white bathtub with a shower curtain, towel rack
      above the sink is a large mirror reflecting the [actor=="Any actor"?"opposite wall":"[actorReference.subject]"]
    Bathroom sink
      https://user.uploads.dev/file/9d1fb8a3708a2e5e55b0c98dc3a72f53.webp
      white oval sink, and chrome faucet, above the sink is a large mirror reflecting the [actor=="Any actor"?"opposite wall":"[actorReference.subject]"]
    Bathroom toilet
      https://user.uploads.dev/file/1e9814375b17911e617c0a9528f0bee0.webp
    Bathtub
      https://user.uploads.dev/file/57aff7bac9e2812d1329b21e5b130dc5.webp
      white [age>=18?"bathtub":"vat"] with a shower curtain
    Bed
      https://user.uploads.dev/file/0a5e9168b5c88eb30c3281014b8e4531.webp
      minimalist bedroom scene with a modern design
      the focal point is a {large|medium|small} bed with {a} {duvet|comforter|blanket that partially slipped off the bed to the floor^2} and {a pillow|pillows}
      the bed is placed against a wall with {a} {headboard|nightstand|lamp|painting|mirror}
    Cage
      https://user.uploads.dev/file/1ed05efd86ccdafbe260349ff898bbe5.webp
    Carpet
      https://user.uploads.dev/file/2c6f5ff0176850f5e73d6527bada6d68.webp
    Chair
      https://user.uploads.dev/file/643a6e5913294d9de7ac18b0885b4fc4.webp
      modern, cozy {kitchen|{living |bed|}room|office} featuring a chair
    Closet
      https://user.uploads.dev/file/f07c9f0366d29f8ce884b6286c1e69bd.webp
      [vibeEra?vibe.lowerCase:"{classical|modern}"] [/luxur/i.test(vibe)?"luxurious":"minimalist"] walk-in closet with a {sleek, monochromatic|simplistic|colorful} design
      built-in drawers and shelves on both sides, with clothes hung neatly
    Corner
      https://user.uploads.dev/file/92550c2a1d6fcc5184e26b4091974f8e.webp
      corner of a room
    Couch
      https://user.uploads.dev/file/c47fc4292e9a72d68a29d22afab51ced.webp
      modern, cozy {guest|living} room
      the focal point is a couch with {a} {coffee table in the center|tv screen on the wall|floor lamp in the corner|rug on the floor|wooden shelving unit with books|modern art on the wall}
    Desk
      https://user.uploads.dev/file/097a1dc0508e713a488d3c0f7c56b673.webp
      [age<=20?"studying":"{home|office}"] desk with a {artistic|sleek, monochromatic|simplistic} design
      the desk is {cluttered with|neatly organized} {papers|books}, {pens|markers} and a {lamp|notebook}
    Door
      https://user.uploads.dev/file/0fe9e12cb26b0bd97da75256e326bc44.webp
    Fireplace
      https://user.uploads.dev/file/0961bbdd0f233b90cdd20cee905664fc.webp
    Fish bowl
      https://user.uploads.dev/file/eabc87877c0ac468c51d6c8ad8abdbea.webp
    Fish tank
      https://user.uploads.dev/file/ad475019c29587d26642570015435c26.webp
    Floor
      https://user.uploads.dev/file/1d743ed8fce49d5a44ce2ef81dd4a466.webp
    Garage
      https://user.uploads.dev/file/b50f1b0557d596f1dc73339056b74c8b.webp
    Hot tub
      https://user.uploads.dev/file/c2fbb39468476950bdb8086d781a11f1.webp
    Jacuzzi
      https://user.uploads.dev/file/868d6d76abfc55f0d5fc966f759267ad.webp
    Kitchen
      https://user.uploads.dev/file/6e9214ae9bda538831a3a5ac64ec0175.webp
    Kitchen counter
      https://user.uploads.dev/file/546c94cc8dda9f5e428bc6b0ce3c4fa1.webp
    Kitchen sink
      https://user.uploads.dev/file/e774109188a4777bd7ce8ee2a7aecddd.webp
    Laundry
      https://user.uploads.dev/file/c8e50dbe7c3e359e016a824800f2cdcb.webp
    Mirror
      https://user.uploads.dev/file/ead062f98736cdb430a9beafad89fd4b.webp
    Pillow
      https://user.uploads.dev/file/c552c6d16ba3d5926af94ad9e7777641.webp
    Refrigerator
      https://user.uploads.dev/file/bab1f67a69bf60c99a6592037f06b1cc.webp
    Rocking chair
      https://user.uploads.dev/file/66efdfcc9221a58cb52a7e61383d719a.webp
    Room
      https://user.uploads.dev/file/4365b3ad3ebf4283a58f1297c9b94aa7.webp
      room of a [age] [gender.lowerCase][age<12?", fluffy animal toys, colorful decorations, and a cozy bed":age<25?", studying desk, books {neatly|haphazardly} arranged on the shelves, posters of {singers|movie stars|sportsmen} on the wall":", the room features items that suggest of a {video gaming|sports|music|art|reading|writing|photography|dancing|fashion|cosplay|traveling|cooking|gardening|fitness|yoga|meditation|martial arts|collecting|DIY|crafting|woodworking|knitting|sewing|painting|drawing|sculpting|pottery|calligraphy|origami|jewelry making|soap making|candle making|baking|brewing|winemaking|cheesemaking|fermenting|pickling|preserving|canning|smoking|grilling|barbecuing} hobby"]
    Rug
      https://user.uploads.dev/file/add782577a7ae2fc961bd7536f6f9ea0.webp
    Shower
      https://user.uploads.dev/file/75db371f1bb4a2401cbbdfb9f83c2be8.webp
      [age>=18?"shower":"bathroom, spraying water coming from the top"] with a curtain
    Sofa
      https://user.uploads.dev/file/ad703d0103c2352169b8028e52202b9f.webp
      modern, cozy {guest|living} room
      the focal point is a sofa with {a} {coffee table in the center|tv screen on the wall|floor lamp in the corner|rug on the floor|wooden shelving unit with books|modern art on the wall}
    Stairs
      https://user.uploads.dev/file/a36e90e1b68b468cedb6208a10ec6905.webp
    Stool
      https://user.uploads.dev/file/47a5c12cf15a8f1f49562b70f6918659.webp
    Stove
      https://user.uploads.dev/file/e9ff6f56273030cb9c6bc2d952f8d58d.webp
    Table
      https://user.uploads.dev/file/5d7414f256562f25fecc559f5d79f262.webp
    Towel
      https://user.uploads.dev/file/bfddb89a3104f2f5fbd7035f981fd29d.webp
    Treadmill
      https://user.uploads.dev/file/2fe3825b2ec22ff75483c378cc4bacdd.webp
    TV screen
      https://user.uploads.dev/file/b7a35c4395248cebcf2bb9b1d2931596.webp
      modern living room scene with the focal point being a flat-screen TV mounted on the wall
      sofa, cushions, and {a} {coffee table in the foreground|rug on the floor|wooden shelving unit with books}
      the TV is turned on, displaying {a} [/romantic|18/i.test(vibe)?"adult movie, {a man and {a woman|two women} are having sex|{a woman|two women} giving a man an oral} on the screen":"{movie|TV show|sports game|news program, the reporter is holding a microphone|weather forecast with a beautiful woman gesturing at a map|music video}"]
      [actorType=="humanoid"?"the [actorReference.subject] is holding the remote control":"the remote control is lying on the sofa"]
    Wardrobe
      https://user.uploads.dev/file/68be3972aa89516a38916106537c5604.webp
    Washing machine
      https://user.uploads.dev/file/b876f4dc5a807a7a12a498c13fe970bd.webp
      washing machine in a {laundry room|bathroom|basement}
    Window
      https://user.uploads.dev/file/93daf3515cd6a9dd18a505d91830d268.webp
    Window seat
      https://user.uploads.dev/file/bba2dbe42e234924ff9536e767193a05.webp
    Yoga mat
      https://user.uploads.dev/file/00603e112dc303fe56ffb5e850438fd1.webp
    <h3><b>Outside</b></h3>
    Alley
      https://user.uploads.dev/file/dcce62e50c016201c01e34842cde49cb.webp
    Balcony
      https://user.uploads.dev/file/c826d45f0e15cdc71d2ba5cb11c241ec.webp
      several adjacent apartments in an apartment buildings with identical balconies
      the central balcony, as well as the neighbouring balconies {are adorned with potted plants|slightly neglected|have flowers in a hanging basket|furnished with a wooden chair|clothing rope drier}
    Beach
      https://user.uploads.dev/file/e5fc866127368e599c9bb71b2f3c03a4.webp
    Bench
      https://user.uploads.dev/file/2f212947352ba3118596ed4c659b5ea5.webp
    Bridge
      https://user.uploads.dev/file/014d129d4f4322d720131c27e989241f.webp
    Canyon
      https://user.uploads.dev/file/4adece9a37e5db933a819b9138f686f4.webp
    Cave
      https://user.uploads.dev/file/301e322c948b1bc6fa0ae0ecc9addc02.webp
    Cliff
      https://user.uploads.dev/file/0cf7e45203905f1f46d659ad2c57d2fe.webp
    Counter
      https://user.uploads.dev/file/173d2bec8c2f66050d32cc856dcbbdeb.webp
      {street food|shop} counter
    Desert
      https://user.uploads.dev/file/b6e682f662930b7fd6b53a04f1ff9d43.webp
    Fence
      https://user.uploads.dev/file/46c547ccd5e7311a6a7cd13d16d119cc.webp
    Field
      https://user.uploads.dev/file/8c00844d67b08d5244e1e65d7a63c4ec.webp
    Flowerbed
      https://user.uploads.dev/file/ff317490c3db5377d700392a2846c9cf.webp
      {circular|rectangular|square|triangular} flowerbed in a paved courtyard, featuring a {circular|cross|star|spiral} design with {red and yellow|pink and white|blue and purple|orange and green|} flowers
    Forest
      https://user.uploads.dev/file/273209c538c8387318821cf849bcc480.webp
    Fountain
      https://user.uploads.dev/file/e7b0061e61e98af079dd592ab95b5edc.webp
      {large|small} {modern|classical|stone|marble} fountain in {a} {garden|park|town square}
      the fountain is surrounded by {trees|flowers|grass|benches|lampposts|statues|buildings} in the background
      the fountain is {crowded with people {walking {in both directions|in one direction}|standing and talking|waiting}|{half-|}empty}
    Garden
      https://user.uploads.dev/file/902809c669981ca5f72d92ae22a2f943.webp
      small garden with vegetation, tree with a swing, garden bench and a lamppost
    Grass
      https://user.uploads.dev/file/95608acbc18a5cfe26605e95f6c1627f.webp
    Grotto
      https://user.uploads.dev/file/1b2c529725324dc55f096b7d17933e59.webp
    Hammock
      https://user.uploads.dev/file/bbbfe5d7e53cb2219b69dad420d9c050.webp
    Haystack
      https://user.uploads.dev/file/3662dd19c6b3af9a8bf5a6420d208443.webp
    Hill
      https://user.uploads.dev/file/0f69fe85faf0e27fdcee615b5725e46f.webp
    Hut
      https://user.uploads.dev/file/7ba921632a53bd11b83e58c6db3593e7.webp
    Iceberg
      https://user.uploads.dev/file/ba452af842fa98c1a5d5d4fb6323970d.webp
    Jungle
      https://user.uploads.dev/file/18de613d54a262c5b6941e37f252f1dd.webp
    Lake
      https://user.uploads.dev/file/293fb66583f13b98ec7040abc90f38f5.webp
    Log fire
      https://user.uploads.dev/file/869ba868a57baf640addd4698c61d15c.webp
      camping spot, log fire in the background
    Meadow
      https://user.uploads.dev/file/a10f3dba8656aa54c9f1123bdc818900.webp
      opening in a forest, a lot of grass and flowers, a couple of trees in the background
    Oasis
      https://user.uploads.dev/file/76811a64436b85e44fb501e1fd9dbc3f.webp
    Ocean
      https://user.uploads.dev/file/a47258ba5531333d73fcbed40adaf111.webp
    Park
      https://user.uploads.dev/file/dad2650c8faff6d79fabe82204f82fe2.webp
      park with a lot of grass and trees{, and swings|}
      walking paths and a couple of benches{, and a lamp post|} in the background
    Parking lot
      https://user.uploads.dev/file/eeb2b36b3effb43453537f7de4ba76c8.webp
    Playground
      https://user.uploads.dev/file/f6fb2bdb4842aa2b45911934ce212d83.webp
    Pond
      https://user.uploads.dev/file/21008db2f5fa13ded469d036941d58e0.webp
    Porch
      https://user.uploads.dev/file/84259f6f6933863a7e74d40a8af7a4ae.webp
    Promenade
      https://user.uploads.dev/file/726d1c5e22efbbc779dc6e19f1c80924.webp
      {river bank|ocean coast|coastal|beach} promenade with a {paved|asphalted} walkway and grass pathway with a railing on one side
      the other side is lined with {apartments|buildings|condominiums|hotels|office buildings|restaurants|shops|[/luxur|punk|urban/i.test(vibe)?"skyscrapers":"park"]|trees}
      the walkway is {crowded with {people|pedestrians} walking {in both directions|in one direction}|{half-|}empty}
    River
      https://user.uploads.dev/file/da01ca9a09bf1d42fec5bc6a75ddc7fb.webp
    Road
      https://user.uploads.dev/file/b3e2c9c741dfd7faf3651918a81eebc9.webp
      road with a {straight|curved} path, surrounded by {trees|buildings|rural area|mountains|fields}[sceneHot?", mirage effect above the road":""]
    Rock
      https://user.uploads.dev/file/020b952a9401c33a8fcb3d07554fc6e4.webp
    Roof
      https://user.uploads.dev/file/3bde3db57e14476b78787c9c833552aa.webp
    Sand
      https://user.uploads.dev/file/a455ec6877d14d3e501eb2aefc4e034d.webp
    Shore
      https://user.uploads.dev/file/6014f7d297671f66f172d2b217c97aa4.webp
    Sidewalk
      https://user.uploads.dev/file/42dbf5cd7d4759134e32d8226d95e217.webp
      sidewalk {adjacent to|separated by {a fence|lampposts|trees|vegetation} from} {a} {parking lot|road with cars} on one side and to {a} {building|hawker stall|fence|park|playground|shop} on the other
      the sitewalk has {a few {people|pedestrians} walking {in both directions|in one direction}|empty}
    Snow
      https://user.uploads.dev/file/bfa78461265eb3ad3dee309c21ceadfd.webp
    Staircase
      https://user.uploads.dev/file/d5c4535e1f5c91bfbb0d80f40aa668c5.webp
      cement {clean, well taken care of|slightly neglected} narrow staircase inside an apartment building with u-turns, landings areas on each level and a railing on the right side
      the landing areas are featuring a very small window and mail boxes with apartment numbers
    Street
      https://user.uploads.dev/file/c2e656279c692d1f69e3ea2bbd1f220a.webp
      bustling city {intersection|street} with {tall|short} buildings on {both sides|one side and {a} {ocean|river|field|forest} on the other}
      {{cars|bicycles|trucks} moving on the main road in the center|pedestrian walking around}
      {streetlights|traffic lights|signs|billboards|posters|graffiti on the buildings}
      {sidewalk|crosswalk|curb|gutter|manhole|sewer|drain|storm drain|storm sewer|storm water drain|storm water sewer} on the side
    Swings
      https://user.uploads.dev/file/69f6c8eb02960bc77a4ce9c756e4bec6.webp
    Tent
      https://user.uploads.dev/file/db3609abe7418d0b393c18494e5bc35f.webp
    Town square
      https://user.uploads.dev/file/d6db64a8c3606ec5cac46909c02388b0.webp
      town square{ with {a fountain|large {paved|asphalted} open space|a large statue} in the center|} is surrounded by {apartments|buildings|condominiums|hotels|office buildings|restaurants|shops|[/luxur|punk|urban/i.test(vibe)?"skyscrapers":"park"]|trees}
      the square is {crowded with people {walking {in both directions|in one direction}|standing and talking|waiting}|{half-|}empty}
    Tundra
      https://user.uploads.dev/file/ff70c1fe7fe755916604361db662bb92.webp
    Underwater reef
      https://user.uploads.dev/file/a5c38d1aa206fb4d4bd73cbb5a5ce91e.webp
    Volcano
      https://user.uploads.dev/file/d49508f114dc53b86c9f3a8ae7db8796.webp
    Wall
      https://user.uploads.dev/file/0171931411c0d6aaab451ca949dae8ea.webp
    Wasteland
      https://user.uploads.dev/file/c5efc224b592e71f06f491ca13b050b6.webp
    Waterfall
      https://user.uploads.dev/file/7e0bce889452d29578c42424a11dde70.webp
    Wheat
      https://user.uploads.dev/file/d60b26cd91a9afeb368971d687aea3bb.webp
    Yard
      https://user.uploads.dev/file/fc69de1943c8c308c92126d4177f7c00.webp
    <h3><b>Places</b></h3>
    Airport
      https://user.uploads.dev/file/1dd5b8b2ca92b0cdb667daac685e8d5b.webp
      airport {terminal with a large, glass-fronted facade filled with people walking around, and a large, digital display board showing flight times|runway with parked airplanes and control tower in the background}
    Backstage
      https://user.uploads.dev/file/3317bf6c945ed3700dbb3cfbeddd4100.webp
      backstage area with a variety of props and equipment
      the room is filled with {costumes|sets|lights|microphones|speakers|monitors|control panels|equipment}
    Barn
      https://user.uploads.dev/file/7e0fe1fd948630186d534889b07300b3.webp
    Basketball court
      https://user.uploads.dev/file/78b8720c6ab1b00d7bb78ca3ed0edff4.webp
      outdoor court with boundary lines surrounded by a chain-link fence[sceneCold?"":" and sparse vegetation in the background"]
      the court is {{half-|}empty|filled with people playing basketball}
    Boxing ring
      https://user.uploads.dev/file/26d9ad66ce0082731c269eabb7d7c41d.webp
    Cafe
      https://user.uploads.dev/file/050597a66fc49883e8fb86cf89e054aa.webp
      cozy, modern cafe interior with a warm, inviting atmosphere
      the room features a mix of natural and industrial elements, including {wooden|metal|plastic|stone} ceiling beams, hanging planters with greenery, and large {black|white|wooden}-framed windows
      several people are seated and engaged in conversation while eating
    Classroom
      https://user.uploads.dev/file/d6a3ab03b9ec959e8efb7d364142ce1d.png
      classroom with large windows on the {left|right} side
      multiple {white|wooden} desks with plastic chairs, each equipped with colorful folders, books, and writing utensils
      a large whiteboard with colorful markers is mounted on the wall
    Club
      https://user.uploads.dev/file/dd6f2e5a2e8496ab4714f8fb160d549d.webp
      nightclub scene with a lively dance floor
      the room is bathed in multicolored lights, primarily red and blue, creating a dynamic atmosphere
      the DJ booth is located at the back of the room, with a large sound system and a DJ spinning records
      the dance floor is filled with people dancing and enjoying the music
    Dancing pole
      https://user.uploads.dev/file/ef74e9dbf62fcb1acfe7752c4523d95c.webp
    Dolphinarium
      https://user.uploads.dev/file/6b5422e28c3d49487af5ce41965c9007.webp
      lively aquatic show in an indoor arena with a large, circular, blue swimming pool at its center
      dolphins performing tricks in the water for the audience
    Dojo
      https://user.uploads.dev/file/b9343ddc0ce82282f581539aaffa5b5d.webp
      traditional Japanese room with a wooden interior
      tatami mat on the floor
      vertical hanging scrolls with Japanese calligraphy
      {katana|bamboo sword} on the wall
    Dungeon
      https://user.uploads.dev/file/7f67931d97ffedf4e0c50537a1056473.webp
      dark, damp dungeon with stone walls and a dirt floor
      the walls are lined with {iron bars|chains|spider webs|mold}
    Escalator
      https://user.uploads.dev/file/edc836182a0423e2ca33ca23569ee652.webp
      busy {shopping mall|train station|subway} featuring {two|three} parallel escalators, with the closest one going {up|down}
      the escalators are {filled with a diverse group of people|half empty|empty}
    Factory
      https://user.uploads.dev/file/eb3be05913ae2eb435ef578f6b68e237.webp
    Farm
      https://user.uploads.dev/file/342c9999087268be76b91f523747cdba.webp
      a rural farm scene with a variety of crops and livestock
      the farmhouse and a barn and a couple other buildings are surrounded by a fence with a tractor parked inside
    Fashion show
      https://user.uploads.dev/file/d495639b8bbaef7c332cce0cc9009993.webp
      a live fashion show on a brightly lit runway
      the audience is seated on both sides of the runway looking at the models walking down the runway
    Fire station
      https://user.uploads.dev/file/c32e5923c1f776950117870f8108d033.webp
      a red-brick fire station with a gabled roof and large garage doors
      bright red fire trucks equipped with ladders and various firefighting equipment are parked in front
    Gas station
      https://user.uploads.dev/file/9b6a95ffbdefc5532b8735492198f01d.webp
      a gas station with a canopy over the pumps
      the pumps are equipped with hoses and nozzles
      the station is surrounded by a parking lot
      the station is brightly lit
    Greenhouse
      https://user.uploads.dev/file/01824bc425e4c9f93f56668e8b21c530.webp
    Gym
      https://user.uploads.dev/file/6fa1eede9d53c43d0ff44fd841c3b40d.webp
    Hawker stall
      https://user.uploads.dev/file/03c6d5efe27a463f1d2467440fccd64a.webp
      a small, open-air food stall with a variety of dishes on display
      the stall is surrounded by a crowd of people waiting to order
    Horse stable
      https://user.uploads.dev/file/bb999b9fda9832e6dcfafeadf597c256.webp
    Hospital
      https://user.uploads.dev/file/086a04e819d0102b3e78537dc82a17b6.webp
    Hotel
      https://user.uploads.dev/file/baf8d9677fc3974aab785e7e81b6944c.webp
      hotel [place="{entrance|hall|hallway|room}".evaluateItem] with a {minimalist|modern|classical} design
      [place=="room"&&actor=="Any actor"?"guests relaxing":"{a person|a couple}".evaluateItem+" {walking|standing and talking|waiting}".evaluateItem]
    Ice maze
      https://user.uploads.dev/file/66b039a8e86f95ac83f6f51e86ff07d3.webp
    Ice rink
      https://user.uploads.dev/file/14f00da87b32c0188c8f94933c459168.webp
    Jail
      https://user.uploads.dev/file/c75c1387fde9e4c83e0591122f0624c1.webp
    Kindergarden
      https://user.uploads.dev/file/5b5a4c5f1f0e3b5c5b5a4c5f1f0e3b5c.webp
      kindergarden classroom with a variety of toys and small size furniture
      the room is filled with children playing and having fun
      the walls are decorated with colorful posters and drawings
    Laboratory
      https://user.uploads.dev/file/75a24fdb9184601dddafd933fbec79da.webp
      modern, sterile laboratory with white walls and a tiled floor
      various scientific equipment and instruments are neatly arranged on the countertops, including test tubes, beakers, flasks, a petri dish and a white microscope
      large, glass-fronted cabinet filled with chemicals and reagents is visible in the background
    Library
      https://user.uploads.dev/file/32acdcb08338a3c5c8b00d9d92781ccb.webp
      well-organized library interior with {wooden book display units|a long, narrow library aisle with wooden bookshelves on both sides, extending into the distance|a traditional library reading room with wooden tables and reading PCs on them|a cozy library reading nook with a comfortable armchair and a small, wooden side table|modern glass-fronted bookshelves and a minimalist design|a curved modern wooden bookshelves positioned centrally that also acts as a registration desk for the library staff with a PC and a chair}
      the shelves are filled with {hardcover |}books of different sizes and colors standing upright
      {{some |}visitors of all ages, mostly young students, are browsing the shelves or sitting at the tables reading books or using their laptops^2|the room is empty}
      the room with {classical ornamented|modern simplistic} ceiling and large windows is filled with a sense of calm and quiet
    Lift
      https://user.uploads.dev/file/b50c241e0ea5b26078c625d88854fcbd.webp
      elevator lobby featuring two elevator doors one of which is open revealing an empty, metallic interior
      doors have digital displays above them
    Locker room
      https://user.uploads.dev/file/c96617092b37dff90cac8210d91e9816.webp
    Movie theatre
      https://user.uploads.dev/file/111ce6fd48e212fe9e3b76f127d6a306.webp
      dimly lit movie theater with rows of upholstered seats arranged in an auditorium-style layout
      the carpet aisle runs down the center of the theater
      the big screen in the background
    Office
      https://user.uploads.dev/file/c37d56d1db43d6ea2c30080f9a98393d.webp
      modern office space with a minimalist design, cubicles and chairs
    Open air concert
      https://user.uploads.dev/file/bed61a6c4977c7430b1bf8e5737a2be4.webp
    Open air museum
      https://user.uploads.dev/file/699177e99619610287fd8ee2f572fae4.webp
      picturesque, outdoor, historical reenactment scene
      variety of historical buildings and structures, including a castle, a church, a windmill, and a farmhouse
      the buildings are surrounded by lush greenery and trees
      cobblestone path winds through the scene
    Opera house
      https://user.uploads.dev/file/da66a9720018241aa2e234a3133e9eb8.webp
      grand, modern concert hall interior with a large, circular stage at its center
      the stage is surrounded by rows of red, upholstered seats arranged in an auditorium-style layout
      the ceiling is adorned with a large, ornate chandelier
    Outdoor market
      https://user.uploads.dev/file/33453d6294f4e0581bf93e6ec602d9cb.webp
      bustling outdoor market with a variety of stalls{ covered with tents|}, each filled with an assortment of {art supplies|accessories|bags|clothing|cosmetics|drinks|electronics|flowers|food|household items|jewelry|shoes|perfumes|books|toys|sporting goods}
      the market is crowded with people, browsing and shopping
    Palace
      https://user.uploads.dev/file/056cc0788d348fe345f6cd82d65ffd09.webp
    Performance stage
      https://user.uploads.dev/file/f34b486097ff6a1083b8fce4aff1b5ae.webp
      brightly lit stage with a wooden floor
      variety of {musical instruments|props|sets|backdrops|lights|microphones|speakers|monitors|control panels|equipment} in the background
      {performers|actors|dancers|singers and musicians|comedians|acrobats|contortionists|illusionists} on the stage
    Photobooth
      https://user.uploads.dev/file/b0da24da16e147a02ddc65ec10860dbd.webp
      rectangular photobooth with a curtain on the front and a camera icon on the side wall
    Planetarium
      https://user.uploads.dev/file/72d7b5835154fbdb00b705a91063d9a8.webp
      dimly lit planetarium room with a domed ceiling and rows of seats arranged in an auditorium-style layout
      digital projection of a starry night sky featuring various planets and constellations on the ceiling
      a massive, translucent Earth projection hovering in the center of the room
    Pool
      https://user.uploads.dev/file/2ce2361516ec64723578495075044533.webp
    Pub
      https://user.uploads.dev/file/92fe2ee2e78588b4845a8a55852a750a.webp
      traditional, cozy pub interior
      wooden bar, adorned with shelves of liquor bottles and glasses
      cushioned wooden barstools
    Restaurant
      https://user.uploads.dev/file/5d25adccea047dba677de2743e7723ad.webp
      modern dining room
      tablecloths covering tables
      wooden chairs with cushions
    Sauna
      https://user.uploads.dev/file/0b0d4626ed440954dbcdd96d3dfe3e5d.webp
      modern sauna room
      the walls and ceiling are clad in light, polished wooden planks
      wooden bench is placed along the wall
      the floor is covered in wooden slats, matching the bench
    School hallway
      https://user.uploads.dev/file/d6b5596df059e38e55a4d6f77eeb3002.webp
      long school hallway with a tile floor
      the hallway is flanked on one side by rows of metal lockers and large windows on the other
    School gym
      https://user.uploads.dev/file/5b768f49cb18e82fe57310975db147df.webp
    Shop
      https://user.uploads.dev/file/aa7325002ced883f4897107085fc8331.webp
      {modern|classical} storefront with a {sleek, monochromatic|simplistic|colorful} design
      large, rectangular windows displaying the goods for sale
      {shelves|racks} filled with {clothing|accessories|shoes|bags|jewelry|cosmetics|perfumes|electronics|books|toys|food|drinks|household items|sporting goods|art supplies|stationery|flowers|plants|pet supplies|tools|hardware|automotive parts|furniture|home decor|kitchenware} seen through the windows
    Shopping mall
      https://user.uploads.dev/file/22b44b3f89441078a3df16e5166c9fd9.webp
      large, modern shopping mall interior with escalators
      variety of stores and kiosks, each with a unique design and color scheme
      the mall is filled with people walking around and shopping
      the floor is made of polished marble
    Skyscraper
      https://user.uploads.dev/file/348dd1791eb1dc7da945144d6bd41e4f.webp
    Soccer field
      https://user.uploads.dev/file/acca1dee6a9451b9d908c59074d7cfa0.webp
      outdoor soccer field with boundary lines surrounded by a chain-link fence[sceneCold?"":" and sparse vegetation in the background"]
      the field is {{half-|}empty|filled with people playing soccer}
    Spa
      https://user.uploads.dev/file/29038fe27ebe393e718ac550bc8e4d01.webp
      serene spa room with a minimalist design
      massage table
      neatly rolled, fluffy white towels, pebbles
      aromatherapy diffuser
      small, wooden table with a glass of water
    Stadium
      https://user.uploads.dev/file/c14d58e9e36229a91ec1ba3a1b4173e7.webp
    Supermarket
      https://user.uploads.dev/file/376398998bf4d7d13a3065979f257667.webp
      large, modern supermarket interior with multiple aisles, each filled with a variety of products
      the aisles are filled with {food|drinks|household items|sporting goods|art supplies|stationery|flowers|plants|pet supplies|tools|hardware|automotive parts|furniture|home decor|kitchenware}
      supermarket {carts|baskets|cash registers|checkout counters|bagging areas|security cameras|security guards|employees|customers|shoppers}
    Studio
      https://user.uploads.dev/file/a37cc5b86a305d45afc0b13fe8c4b2d8.webp
      dim lit room of a tv studio
      variety of {cameras|lights|microphones|props|sets|backdrops|green screens|monitors|control panels|equipment} in the background
      the studio is filled with {crew members|actors|directors|producers|technicians|staff} working on the set
    Tavern
      https://user.uploads.dev/file/766857cdf56e5c8e74ac0d85ec739947.webp
    Train station
      https://user.uploads.dev/file/5da2a3ad11267471441f0dabb11a31d6.webp
      large, modern train station with several platforms, each filled with a variety of trains and people waiting
    Warehouse
      https://user.uploads.dev/file/7e6ef820e07f4d049608c89fbbc002be.webp
      large, empty warehouse with a concrete floor, metal walls and rows of shelves
      the ceiling is high and made of metal
      the shelves are filled with {pallets|boxes|crates|barrels|containers|machinery|equipment|tools}
      loading forklift vehicle in the background
    Waterpark
      https://user.uploads.dev/file/d09566c012e4b33a3dec7dcadf71691a.webp
      large, modern waterpark with a variety of water slides, pools, and attractions
      the waterpark is filled with people enjoying the water
      the floor is made of concrete
      the water is clear and blue
    Zoo
      https://user.uploads.dev/file/89ef91f21dbae16509ee6a206d51a537.webp
      zoo enclosure with a {glass|metal|wooden} fence
      the enclosure is filled with {grass|sand|rocks|water|trees|plants|vegetation}
      the wild animals are {walking|running|playing|resting|eating|drinking|sleeping} in the background
    <h3><b>Transportation</b></h3>
    Airship
      https://user.uploads.dev/file/0a94c86dbf5d3b97802337366eaee91e.webp
    Boat
      https://user.uploads.dev/file/2841065f52fc539d4ee548ebdd0fca41.webp
    Bus
      https://user.uploads.dev/file/0ff23708af86fbe120513e208ea9e290.webp
      modern bus interior with a bus driver's cabin, a variety of seats and handrails
      the bus is {filled with passengers of all ages sitting and standing|{half-|}empty}
      the bus is {moving along a wide road|stopped at a bus stop|stopped at a traffic light} with varierty of other cars and buildings in the background
    Bicycle
      https://user.uploads.dev/file/a8d18882e82d02917a95244406fb5a88.webp
    Car
      https://user.uploads.dev/file/078afb258141db778f3cd272a4ff5e2b.webp
      car {driver's seat, steering wheel in front, dashboard with a speedometer and other indicators|backseat|passanger's seat}
    Cart
      https://user.uploads.dev/file/28bdda830accb11166ca091e000f9b76.webp
    Cockpit
      https://user.uploads.dev/file/91c420e70129b7dd1431c9c27ce20f8d.webp
      cockpit of a {plane|helicopter}
      control panel with a variety of buttons, switches, levers, and indicators
    Cruise liner
      https://user.uploads.dev/file/aeb811b35826ec623dae19835a168a55.webp
    Helicopter
      https://user.uploads.dev/file/7f8a87976b0eb0e06bfe42919433630f.webp
    Horse
      https://user.uploads.dev/file/7f8e17fbc738472c5d21bf68f39c4e49.webp
    Hot air balloon
      https://user.uploads.dev/file/8b457ce1cca7a03bb11367472bde4acc.webp
    Motorboat
      https://user.uploads.dev/file/ed2504d140cf43564d27a6223c35af0b.webp
    Motocycle
      https://user.uploads.dev/file/4fcef871c3ba99ac509aee545a1cce10.webp
    Paraglider
      https://user.uploads.dev/file/a2573bf5282dc99b66b35b65cba48431.webp
    Plane
      https://user.uploads.dev/file/61ccc4d706ef40fc086c61cd085b27c1.webp
    Rocket
      https://user.uploads.dev/file/a2c86ae0059123094e6ab63b80025812.webp
    Rowboat
      https://user.uploads.dev/file/76a989bd1b2e7ebf2a330b439263e31f.webp
    Sailboat
      https://user.uploads.dev/file/c98214fd07f2bbbd890f5d8870d41b65.webp
      sailboat {interior with a wooden floor|stern|deck|bow|mast}
    Scooter
      https://user.uploads.dev/file/d5181986be5267abcbf9b8322688708c.webp
    School bus
      https://user.uploads.dev/file/cbb81cf3ab710fbf7987eddc20176e79.webp
    Ship
      https://user.uploads.dev/file/3bda337ce3c5efab188e9c8b2630b334.webp
    Steamer
      https://user.uploads.dev/file/77b0543c5d86cdf1b1b578e7db268ffa.webp
      steamer ship, smoky atmosphere
      large, wooden deck with a variety of {cargo|passengers|crew members}
    Submarine
      https://user.uploads.dev/file/78faa953e77e9d15c0e3d3cb9852da5d.webp
      submarine control room, featuring a dense array of complex machinery and equipment
      the control panel, located centrally, is cluttered with numerous dials, switches, levers and gauges
      the floor is covered in green carpeting, and various pipes and cables are visible overhead
    Subway
      https://user.uploads.dev/file/7c87bf673af01b8acf6074129561bfbf.webp
      subway station
      subway train in the background
      couple of people waiting for the train on the platform
    Tractor
      https://user.uploads.dev/file/5915e66acf3ec8a1b7ff1e7328b9fb5d.webp
    Train
      https://user.uploads.dev/file/5b6752e76c4ac2cfbe93c1a9a41aa376.webp
    Tram
      https://user.uploads.dev/file/18c8ca5d007e0f104f4d224ae00fcabc.webp
    Truck
      https://user.uploads.dev/file/a22b2f06bba22e1c940e4c72c932606e.webp
    Van
      https://user.uploads.dev/file/2d53b2d56286602ad02fdf3192d65fd9.webp
    Yacht
      https://user.uploads.dev/file/920fd1209ea8c5fa0e6239ea19777175.webp
    <h3><b>Highlights</b></h3>
    Alien relic
      https://user.uploads.dev/file/5c7d8d60bf912d71401065e26911c344.webp
      million years old alien relic site shrouded in {mist|unnatural glow|outer planetary lights|localized weather effects|parrenial thickets|overgrown vegetation|alien vegetation}
      alien {stone|metal|crystall|glass|organic} megastructure of unknown nature with ancient glowing outer planetary {patterns|symbols|schematics|ornaments} and big {portal|eye|glass construction|DNA-like form|{abstract|geometrical} object} in the middle in the background giving eerie feeling
    Big Ben
      https://user.uploads.dev/file/5b422da1b7dd0a547ad2d4a0f5ca3541.webp
    Chernobyl
      https://user.uploads.dev/file/20de29608baa0a0aaee26f0bd623d634.webp
      Chernobyl Exclusion Zone
      {abandoned buildings|abandoned cars|abandoned machinery|abandoned vehicles|abandoned monuments} in the background
      {radiation|fallout|nuclear} warning signs
      {radiation|fallout|nuclear} warning posters
      {radiation|fallout|nuclear} warning {placards|billboards}
    Chichen Itza
      https://user.uploads.dev/file/2483923677c3c88a58ec19cc0e08bac9.webp
    Christ the Redeemer
      https://user.uploads.dev/file/758b772e9b9df051d1dd9b21ab20641f.webp
      Christ the Redeemer statue on top of the Corcovado mountain in Rio de Janeiro
    Colosseum
      https://user.uploads.dev/file/dda18709edc56dd25e2f26f915fca6ff.webp
    Eiffel Tower
      https://user.uploads.dev/file/9248870c0294e192d00254d066cad2cf.webp
    Forbidden City
      https://user.uploads.dev/file/72a06bffad83c5cfce5a6d459aaed754.webp
      Forbidden City in Beijing
    Great Wall of China
      https://user.uploads.dev/file/38044244d81f28140c4ce8be1b127949.webp
    Hermitage
      https://user.uploads.dev/file/49e199de7dc25bc2902059fcc2f91bb2.webp
    Kremlin
      https://user.uploads.dev/file/14b01cd6b5e1e1a3fad5ae0e5aa8aa01.webp
    Leaning Tower of Pisa
      https://user.uploads.dev/file/5a20cfe1eb793a7f097dc5385dfb6214.webp
    Louvre
      https://user.uploads.dev/file/92e0fdecbe827a554afe89d0544763dc.webp
      Louvre Museum in Paris
    Lost city of Atlantis
      https://user.uploads.dev/file/d6b2edce2a45281885b63299d89b34d8.webp
      underwater ruins of an ancient city on the bottom of the sea
    Machu Picchu
      https://user.uploads.dev/file/468dc2f3841f6555d326b1c3bade1b40.webp
    Niagara Falls
      https://user.uploads.dev/file/de9217fd7ec6e3e4e963372261369306.webp
    Notre Damme de Paris
      https://user.uploads.dev/file/7208908b9eea30ab7d2deb1676aa98f1.webp
    Pantheon
      https://user.uploads.dev/file/f73c0c2c45dbaa8d1b9201220157eb60.webp
      Pantheon in Rome
    Persepolis
      https://user.uploads.dev/file/305d8b77ea4902dbbcbaecd8aa68bf44.webp
    Petra
      https://user.uploads.dev/file/646cd661265083ecc8381eea278c10a4.webp
    Pyramids
      https://user.uploads.dev/file/0ae259a9b61bfa71ef38f48de89a838c.webp
      Great Pyramid of Giza in the background
    Saint Basil's Cathedral
      https://user.uploads.dev/file/8c99589abbc91caa017d988a978b73b0.webp
    Sphinx
      https://user.uploads.dev/file/87b4c34f9d328a25354e797a23b60a22.webp
      Sphinx in Giza
    Statue of Liberty
      https://user.uploads.dev/file/946c6b46c3f5324269b6a1b6797502d7.webp
    Stonehenge
      https://user.uploads.dev/file/05a40e44cf4c5487feb46bcf21821911.webp
    Sydney Opera House
      https://user.uploads.dev/file/45ca724ba1966fea9e2944d6a80d3f45.webp
    Taj Mahal
      https://user.uploads.dev/file/20ad560fbbc7525bbd12f8b354f071c3.webp
    Temple of Heaven
      https://user.uploads.dev/file/eb45c1bc02c2a9cbd049226d5220de1e.webp
      Temple of Heaven in Beijing
    Victoria Falls
      https://user.uploads.dev/file/2b8963de669ac78ed0309328a67efc3e.webp
    Washington Monument
      https://user.uploads.dev/file/94655eb4fc8c59afb81df79221ee557f.webp
    White House
      https://user.uploads.dev/file/962e0a2cde6a91f880d13d39503509b8.webp
      White House in Washington
    Ziggurat of Ur
      https://user.uploads.dev/file/c11e86ee85f07263956b74d8f1beba02.webp
    <h3><b>Space</b></h3>
    Black hole
      https://user.uploads.dev/file/34cf5515ba7b9d2fb0fe3c9add7fe262.webp
      void in the background
      accretion disk around the black hole
      gravitational lensing effect
    Earth orbit
      https://user.uploads.dev/file/3e3a76cfcadea2c7f232a8f344890e40.webp
      low Earth orbit
      Earth clouds, oceans, continents in the background
    Jupiter surface
      https://user.uploads.dev/file/63affa27611c18b6cbd3a36d61f34932.webp
      dense liquid atmosphere of hydrogen and helium
      clouds everywhere, dim lighting
      high pressure, high temperature, high gravity
      lightning strikes
      gigantic winds[hairLength!="Bald♂️"?[actorType=="humanoid"?" messing the hair"+[camera!="top"?" and strongly blowing the clothing":""]:actorType=="animal"?" moving the fur":""]:""]
    Mars surface
      https://user.uploads.dev/file/5a73bf13c39109bc8dede08d775d1638.webp
      Mount Olympus Mons far in the background
      {Mars colony in the background|red dust storm|}
    Moon surface
      https://user.uploads.dev/file/e9b15e38fc5596bce80d4bb87413df5e.webp
      Earth far in the background
      moon colony in the background
    Space
      https://user.uploads.dev/file/137f28af46d061362a4140d545a072c4.webp
      {stars|a space station|a space ship} in the background
    Space station
      https://user.uploads.dev/file/635792036be4e6a563691bdef50a59ea.webp
      space station interior
      variety of {scientific equipment|computers|monitors|control panels|equipment} in the background
    Spaceship
      https://user.uploads.dev/file/5b4e410982f7dea01fbb03da12329eed.webp
      cockpit of a spaceship
      a variety of {scientific equipment|computers|monitors|control panels|equipment} in the background
    Venus surface
      https://user.uploads.dev/file/4d7959b9f011b93ac9f74bdcb06ceae4.webp
      extremely hot
      air mirage effect
      extremely high pressure
      high concentration of acids
      {boiling stones and acid rain|}
  lighting
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="lighting=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="lighting" ${item.getName==lighting?'checked':''} /><label>${item.getName == 'Any lighting'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any lighting
    Aurora
      https://user.uploads.dev/file/6e22058367c4c578b40f3f92e35e7313.webp
      the Northern Lights are diffuse and spread out in wispy, ribbon-like patterns across the sky, creating a dynamic and ethereal visual effect in contrast to the dark blue and black sky[sceneOpenAir?"":" outside"]
    Bright lamp
      https://user.uploads.dev/file/a585c21e958417548b0fc1c5b75d7633.webp
      bright white fluorescent light coming from a number of [!sceneOpenAir?"spot lamps on the ceiling and the walls":"lamp posts in the background"]
    Candle
      https://user.uploads.dev/file/5841c245094937380610c9ed19c725aa.webp
      {a number of |a few |}candles{ in candlesticks|} are lit illuminating the scene
      [actorType=="humanoid"?[sceneHandsFree?"[actorReference.subject] holding a candle{, its light is reflected in the eyes|}":""]:""]
    Day
      https://user.uploads.dev/file/3ec05ffa5f58c85c8452b44025d86895.webp
      [/cloudy|rainy|snowy/i.test(weather)?"the sun is creating highlight on the edges of clouds and making their interior darker, the light is diffused and evenly illuminates the scene":"sunlit scene with vibrant colors"]
      [/cloudy|rainy|snowy/i.test(weather)?"":"bright midday sun rays coming top-down from the zenith through the "+[sceneOpenAir?[sceneVegetation?"{trees|leaves|branches}":"clear sky"]:"[windowType]"]]
    Fireworks
      https://user.uploads.dev/file/d3b390edbbf1ca4f1e4a129361057a39.webp
      fireworks against {a} [/cloudy|rainy|snowy/i.test(weather)?"overcast":"clear"] dark sky[sceneOpenAir?"":" outside the [windowType]"] illuminating the scene with a bright colorful light
    Lightning
      https://user.uploads.dev/file/feb4e1c1cf32decfea18cf1407036df4.webp
      lightning strike brightly illuminating the scene
    Neon
      https://user.uploads.dev/file/d05a39c0bd1fc577c02abe7e66b67756.webp
      neon {lights|advertisements|signs}[sceneOpenAir?" in the background":" outside the [windowType]"]
      the neon lights are bright and colorful, creating a vibrant and dynamic visual effect
    Night
      https://user.uploads.dev/file/671a9f42d99aefd67c062f75facfc084.webp
      midnight scene with dark colors
      [/cloudy|rainy|snowy/i.test(weather)?"overcast dark sky with no visible stars or moon":"{moon|Milky Way|bright stars} far in the sky"]
      [!sceneOpenAir||sceneCold?"":"a couple of fireflies in the air adding to overall illumination"]
    Solar eclipse
      https://user.uploads.dev/file/9788c534a1e61ec829d613b818a1edde.webp
      total solar eclipse[sceneOpenAir?"":" outside"] featuring the sun[/cloudy|rainy|snowy/i.test(weather)?" peeking through the clouds":""] completely obscured by the moon's shadow, its corona providing a subtle illumination against the otherwise dark sky
    Spotlight
      https://user.uploads.dev/file/4e2f96a7c6940266bcc398ff8bb8dcc6.webp
      spotlight is casting a bright, focused beam of light that creates a sharp contrast between the illuminated area and the surrounding darkness
      [actor=="Any actor"?"":"the spotlight is focusing on the [actorReference.subject]"]
    Studio
      https://user.uploads.dev/file/94c98daed25ec8331d634a6e7c0aca56.webp
      two studio lights focusing on the center of the composition from both sides, creating a soft, even illumination with minimal shadows
      the background is evenly lit, with no harsh shadows or highlights, creating a clean, professional look
    Sunrise
      https://user.uploads.dev/file/5c7797eac59babdfbddf671a88ddb495.webp
      sunrise lighting is soft and diffused, the [/cloudy|rainy|snowy/i.test(weather)?"sun that is about to rise is painting the clouds orange and pink":"sky transitioning from a deep blue at the top to a lighter blue near the horizon, indicating the sun is about to rise"]
    Sunset
      https://user.uploads.dev/file/1589fee2867c6adeb1a500bc30ff508a.webp
      sunset lighting is soft and diffused, the [/cloudy|rainy|snowy/i.test(weather)?"sun that is about to set is painting the clouds orange and red":"sky transitioning from a deep orange at the top to a lighter orange near the horizon, indicating the sun is about to set"]
    Twilight
      https://user.uploads.dev/file/b9ab854deeaf6dbec4acf7bec8666110.webp
      twilight lighting is soft and diffused, with the [/cloudy|rainy|snowy/i.test(weather)?"sky overcast by clouds":"sky transitioning from a deep blue at the top to a lighter blue near the horizon, indicating the sun has recently set or is about to rise"]
    Yellow Lamp
      https://user.uploads.dev/file/8593faa7c1426c9786104edb8f44ab41.webp
      gentle warm lighting is diffused and soft, emanating from a [!sceneOpenAir?"{square|round}-shaped "+[/attic|bed|chair|couch|desk|fireplace|room|sofa|spa|TV/i.test(scene)?"bedside":/edge/i.test(sceneDimensions)?"table":"hanging"]+" lamp with a slightly textured lampshade":"lamp posts in the background"] creating a calming, ambient effect
  weather
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="weather=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="weather" ${item.getName==weather?'checked':''} /><label>${item.getName == 'Any weather'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any weather
    Breeze
      https://user.uploads.dev/file/b51b9e649e18120a8861b527613b8012.webp
      gentle[sceneOpenAir?" breeze":" draft"][hairLength!="Bald♂️"&&actorType=="humanoid"?" slightly moving the hair":""]
    Clear
      https://user.uploads.dev/file/5ef4d224cbe78a249d1105e4d4d8aa6d.webp
      crystal clear skies with no visible clouds[sceneOpenAir?"":" outside the [windowType]"]
      [lighting=="Day"?"depth to the clear skies":""]
    Cloudy
      https://user.uploads.dev/file/5b1df314d9d17560007dbf7b521637d2.webp
      the sky[sceneOpenAir?"":" outside"] is covered with a thick layer of {dark stormy |white fluffy |}clouds
    Foggy
      https://user.uploads.dev/file/6fe8045c4ec17248c4dfc4239c1e1deb.webp
      thick fog [sceneOpenAir?"everywhere":"outside"] obscuring the background 
    Rainy
      https://user.uploads.dev/file/0f187cdc7f2e49ddef0dc48027a6cc9c.webp
      [lighting=="Day"?"{rainbow, |}sunshower drizzling":"{rain pouring down|drizzle falling}"][sceneOpenAir?"":" outside"]
      [camera=="top-mid-low"?styleList.filter["camera weather effects"].selectAll.joinItems(", "):""]
    Snowy
      https://user.uploads.dev/file/ebe6f4d3af6d21ea035d54f7302cbc66.webp
      massive snowfall at high speed and angle[sceneOpenAir?[actorType=="humanoid"&&camera!="mid"&&camera!="low"&&!/rear/i.test(camera)&&eyeWear=="Any eyewear"&&mood!="Eyes closed"&&!/sleep/i.test(pose)?" making [actorReference.subject] squint the eyes":""]:" outside the [windowType]"]
      [camera=="top-mid-low"?styleList.filter["camera weather effects"].selectAll.joinItems(", "):""]
    Windy
      https://user.uploads.dev/file/c817540f12d5ee054d80988d2e2df4ac.webp
      [sceneOpenAir?"wind"+[hairLength!="Bald♂️"?[actorType=="humanoid"?" messing the hair":actorType=="animal"?" slightly moving the fur":""]:" blowing "+[sceneDirty?"garbage pieces":sceneCold?"snowflakes":sceneVegetation?"trees and leaves":"dust"]]:""]
      [sceneOpenAir?[!sceneNude&&actorType=="humanoid"&&camera!="top"?"wind blowing the clothing":""]:""]
      [sceneOpenAir?[sceneWet?"wind blowing water drops and disturbing the water surface":""]:""]
  vibe
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="vibe=this.value" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="vibe" ${item.getName==vibe?'checked':item.getName=='<h3><b>Atmosphere</b></h3>'||item.getName=='<h3><b>Background</b></h3>'||item.getName=='<h3><b>Era</b></h3>'||item.getName=='<h3><b>Season</b></h3>'?'disabled':''} /><label>${item.getName == 'Any vibe'||item.getName=='<h3><b>Atmosphere</b></h3>'||item.getName=='<h3><b>Background</b></h3>'||item.getName=='<h3><b>Era</b></h3>'||item.getName=='<h3><b>Season</b></h3>'? '' : '<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Any vibe
    <h3><b>Atmosphere</b></h3>
    Colorful
      https://user.uploads.dev/file/8804b50a40c39bd139e81a36a7ffb545.webp
      vibrant natural colors
      saturated foreground
      bright background
    Cosy
      https://user.uploads.dev/file/e6cf3b7e2754cb0ec34063dc4bf34e0f.webp
      warm palette[!sceneOpenAir?", cushioned well-taken care of "+[sceneTransportation?"seats":"furniture"]:", pleasant view of the {nature|clean street}"]
      [actorType=="humanoid"?"blanket on the shoulders":""]
    Dramatic
      https://user.uploads.dev/file/00c74992a763dfc6afb988f9883c8ea1.webp
      dramatic movie filters and effects
      emotion stirring cinematics
      pronounced bukeh effect
    Dreamy
      https://user.uploads.dev/file/cef6b91f49e81c80161c019706742b00.webp
      slightly foggy and blurry scene with a collage of giant translucent [actorType=="humanoid"?"{alient planet|cake|Earth|female [chest]|Jupiter|[hole]|luxury car|Mars|Moon|spaceship|waterfall and palm trees}":actorType=="animal"?"{food|toy|treat}":"{alient planet|field|Jupiter|Mars|Moon|waterfall}"] in the background representing a desire and wonder during a dream
      the composition uses a soft, dreamy color palette with vibrant colors
      the image has a surreal, whimsical style, evoking a sense fantasy
    Fresh
      https://user.uploads.dev/file/546659c5142fd8cb752ae0c60567d0b4.webp
      [sceneOpenAir?"well taken care of environment":"fresh and clean wiped floors and windows"]
    Gloomy
      https://user.uploads.dev/file/5125f146ab18ca0335c0dce760492416.webp
      gloomy and dark palette, evoking a sense of sadness
    Horror
      https://user.uploads.dev/file/d3dcd7015e0c90d5dd115e272f05d973.webp
      horror movie effects and filters
      the composition uses a dark palette to create a sense of dread and unease
    Luxury
      https://user.uploads.dev/file/dcba28578e5d6975a55c788043a0e255.webp
      luxury [sceneOpenAir?[sceneWet?"yachts":"{cars|houses}"]:sceneTransportation?"leather upholstered seats":"furniture"] in the background
      [actorType=="humanoid"?"wearing luxury "+[!sceneNude?"clothing":""]+" and {jewelry|watch}":""]
    Magical
      https://user.uploads.dev/file/08a0a3b83bbad2ac108d337932c9fe9d.webp
      magical {dust|particles|spells going off|effects} in the air
      [actor!="Any actor"?"magic aura around the [actorReference.subject]":""]
    Messy
      https://user.uploads.dev/file/422f330dba7cf439cb92f7371410ae82.webp
      dust particles in the air
      [!sceneOpenAir?"clothing and everyday objects thrown randomly on the floor and the "+[sceneTransportation?"seats":"furniture"]+", dirt smudges on the walls, a layer of dust on the floor":"garbage thrown randomly on the ground, poorly taken care of environment, dirt smudges"]
    Mysterious
      https://user.uploads.dev/file/b642ee3fb43520e0be2ae128999c4496.webp
      mysterious cinematic framing
      mysterious cinematic filter and effect
      less color on the frame edges
      vignette effect
    Party
      https://user.uploads.dev/file/15b3ebd747097f5a3d8b9cfc5283fe17.webp
      vibrant palette
      party tables and chairs in the background
      party beverages and cakes on the tables in the background
      party decorations and balloons
      [sceneOpenAir?"party barbeque setup":"huge party music system"]
      [actorType=="humanoid"&&headwear=="Any headwear"?"wearing paper party hat":""]
    Romantic
      https://user.uploads.dev/file/f4b56a44043d38f0959628efa75cee86.webp
      the composition uses warm light palette consisting mostly of golden and amber colors
      [actor!="Any actor"?"the backlight separates the [actorReference.subject] from the background creating a sense of closeness and romance":""]
      [actorType=="humanoid"?"a {red rose|chocolate box|love letter} in the "+[actorHandsFree?"[actorReference.subject]'s hands":"background"]:""]
    Simplistic
      https://user.uploads.dev/file/0c6b2561ba4feff82acff1e60c1dc6f0.webp
      minimalistic but well taken care of[sceneOpenAir?" environment":sceneTransportation?" seats":" furniture"]
      serene pastel colors
    18+ movie
      https://user.uploads.dev/file/764620c9470c973a994d7f051de55e2d.webp
      [age>=18?"highly erotic ":""]composition uses a dark palette evoking a sense of closeness and desire
    <h3><b>Background</b></h3>
    Animals
      https://user.uploads.dev/file/e8971b08383ad7930315cc0de02381ad.webp
      a couple of [sceneVegetation?"wild animals":sceneOpenAir?"domestic animals":"pets"][sceneOpenAir||sceneWindowless?" in the background":" seen through the window"]
      [actorType=="animal"&&pose=="Any pose"?"the [actorReference.subject] and the animals are playing together":""]
    Crowd
      https://user.uploads.dev/file/ae2fd5cf45fefc900d75a690e70c0de5.webp
      silhouettes of different people [sceneLocation||sceneHighlights?"visiting the crowded "+[sceneHighlights?scene:scene.lowerCase]:"in the crowd walking {towards|away from|to the side of|past} the camera and talking"]
    Few people
      https://user.uploads.dev/file/695d8028760d2ebab1fc22f3d2f1088f.webp
      a couple of silhouettes of different people [sceneLocation||sceneHighlights?"visiting the "+[sceneHighlights?scene:scene.lowerCase]:"walking {towards|away from|to the side of|past} the camera"]
      [weather=="Rainy"&&sceneOpenAir?"the people are hurrying and shielding the head from the rain":""]
    Fire and smoke
      https://user.uploads.dev/file/3f4d0a162030fbd8f7c3083ba9ef1873.webp
      fire and smoke in the background
    Flowers
      https://user.uploads.dev/file/6425e4387700044d2e7484b69b69e4f8.webp
      a lot of {daisies|dandelions|lavenders|lilies|lotuses|orchids|peonies|poppies|sunflowers|violets|water lilies|wisterias|daffodils|hyacinths|irises|magnolias|pansies|roses|tulips|flower bouquets} in the background
    Rural landscape
      https://user.uploads.dev/file/7b3043f4c017eb16ac189e283540fc89.webp
      rural landscape of a {farm|village|countryside} with ["{fields|hills|mountains|trees|rivers|lakes}".selectMany(2).joinItems(", ")][sceneOpenAir?" in the background":" outside the [windowType]"]
    Small town landscape
      https://user.uploads.dev/file/fe225d2aa05db30b2b8694691a953143.webp
      small modern town with ["{bridges|cars|houses|lampposts|parks|shops|squares|streets|trees along the roads}".selectMany(2).joinItems(", ")], very few people walking around[sceneOpenAir?" in the background":" outside the [windowType]"]
    UFO
      https://user.uploads.dev/file/da07d4c8fa587ed5518fd26304495cf1.webp
      UFO [sceneOpenAir?"in the background":"outside the [windowType]"] 
    Urban landscape
      https://user.uploads.dev/file/0a35533bd609a116c6088a9b5f6a5764.webp
      urban landscape of a modern city with ["{skyscrapers|well-designed buildings|roads|bridges|tunnels|traffic lights}".selectMany(2).joinItems(", ")], bustling with people activity[sceneOpenAir?" in the background":" outside the [windowType]"]
    Vehicles
      https://user.uploads.dev/file/d2f710420d61706654a313e4eb56ea04.webp
      ["{cars|trucks|buses|trains|trams|ships|boats|yachts|airplanes|helicopters|spaceships}".selectMany(2).joinItems(", ")][sceneOpenAir?" in the background, contrail across the skies":" seen through the window, smog from the transport"]
    <h3><b>Era</b></h3>
    Ancient Egypt
      https://user.uploads.dev/file/be93d0c95f7d55c73d5240d0c273b202.webp
      ancient Egypt {hieroglyphs|symbols}
    Ancient Rome
      https://user.uploads.dev/file/99c39a67167a6d207e009405c22ad77b.webp
      ancient Rome {statues|symbols}
    Cyberpunk
      https://user.uploads.dev/file/a450fd8d6b0d9181adce518e75a5dca8.webp
      [sceneOpenAir?"cyberpunk {neon sings, neon lights and buildings|city}":[sceneWindowless?"":"cyberpunk city outside the [windowType]"]]
      [actorType=="humanoid"&&accessories!="None"?"cyberpunk {eye gadgets|prosthetics|implants|cyberware}":""]
    Futuristic
      https://user.uploads.dev/file/d6e1491853b8e55e53c618ea04f9b9db.webp
      [sceneOpenAir?"{skyscrapers|spires|domes|flying cars|flying drones|high-speed trains|spaceships lifting}".selectMany(2).joinItems(", "):"minimalistic but elegant furniture made of {plastic|glass|unknown material}, {hologram|big TV screen|device of uknown nature}"]
    Medieval
      https://user.uploads.dev/file/5fde433b3613d673c1904acc2f178c70.webp
      a medieval {cart|horse|castle|mill|palace|cobbled road}[sceneOpenAir?" in the background":" seen from the window, simple medieval furniture"]
    Post-apocalyptic
      https://user.uploads.dev/file/b8c7fcc9ae6f2d70e0e008a4c04bcb7e.webp
      [sceneOpenAir?"{ruined buildings and roads|ruined cars and famous monuments|ruined trees and nature}":sceneTransportation?"broken seats":"broken furniture remains"]
    Prehistoric
      https://user.uploads.dev/file/6dbb761df907c1f767942e39eb434d01.webp
      [actorType=="humanoid"?"[actorReference.subject] wearing prehistoric {weapons|trinkets}":""]
      dinosaurs[sceneOpenAir?" in the background":" seen through the cave's entrance, fire place inside a stone circle in the middle of the cave"]
    Renaissance
      https://user.uploads.dev/file/0f2b76130059f981f44da56c28cee806.webp
      [sceneOpenAir?"{carts|frigates}":"Renaissance {paintings|sculptures}"]
    Soviet
      https://user.uploads.dev/file/71a03cb37e33f2fb7ff740a34ed574b4.webp
      [sceneOpenAir?"soviet cars and buildings":"{Lenin sculpures, busts and paintings|Stalin paintings|Gagarin posters|Leonov posters|Gorbachev Glassnost and Perestroika posters}"]
    Steampunk
      https://user.uploads.dev/file/e348636e82f018bac3134d279e1f29a6.webp
      [sceneOpenAir?"steam trains and airships":"{gears and cogs|steam engines and steam pipes with valves}"]
    Wild West
      https://user.uploads.dev/file/e92fe4e176a4a4d26341afc0d370f45a.webp
      [sceneOpenAir?"{horses|saloons|outlaw posters}":"simplistic wooden furniture, self-playing piano, wild west posters"]
      [actorType=="humanoid"&&!sceneNude?[headwear=="Any headwear"?"wild west hat":""]+[camera=="top"?"":", revolver in the holster"]:""]
    50s US
      https://user.uploads.dev/file/81855aaceb82409af959fcf3171dbac7.webp
      [sceneOpenAir?"50s US cars"+[!sceneVegetation?" and , 50s US {gas stations|motels|diners}":""]:"{Marilyn Monroe|Elvis Presley} posters"]
    80s US
      https://user.uploads.dev/file/06d925da41723e22d6ba22999977ff64.webp
      [sceneOpenAir?"80s US cars"+[!sceneVegetation?" and , 80s US arcades and neon signs, rock bands posters":""]:"{shuttle program|80s US music band} posters"]
    <h3><b>Season</b></h3>
    Autumn
      https://user.uploads.dev/file/a18b22d373eaf21e66ca8c3bbc54306f.webp
      autumn {flowers and |}trees [sceneOpenAir?"in the background{, falling lea{f|ves}|}":"outside the [windowType]"]
    Christmas
      https://user.uploads.dev/file/be362bbd1b6aa7b663fe7ab4c751a819.webp
      christmas tree and decorations and lights[sceneOpenAir?"":", christmas presents and stockings"]
      [actorType=="humanoid"&&headwear=="Any headwear"?"santa hat":""]
    Spring
      https://user.uploads.dev/file/f2c53c45ef3721437c224c355bcf6fb7.webp
      spring {flowers and |}trees [sceneOpenAir?"in the background{, flying blooming cherry blossom petal{s|}|}":"outside the [windowType]"]
    Summer
      https://user.uploads.dev/file/05b94d75e10a9fa3eb6360324760fc66.webp
      summer {flowers and |}trees [sceneOpenAir?"in the background{, floating dandelion seed{s|}|, flying butterfl{y|ies}|}":"outside the [windowType]"]
    Winter
      https://user.uploads.dev/file/9260048486db0ced026ad3f2f57759ed.webp
      winter snow and snow covered trees [sceneOpenAir?"in the background{, falling snowflakes|}":"outside the [windowType]"]
 //<=Scene   
styleList // style, resolution, filter, artist
  style
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="style=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="style" ${item.getName==style?'checked':''} /><label>${item.getName=='Any style'?'':'<img src='+item.url+'>'}${item.getName}</label></div>`).join('')]
    Any style
    Photo📷
      prompt
        real life photography, RAW photo
      negative
        3D, octane render, cartoon, 3D cartoon, anime, drawing, painting, illustration, doll
      url
        https://user.uploads.dev/file/9ef8c190ed38eaca40d602c713b63e38.webp
    Anime🎨
      prompt
        realistic digital anime style
        exceptional photorealism
        the artist uses soft, warm colors and detailed shading to enhance the realism
      negative
        3D-render, photo, doll
      url
        https://user.uploads.dev/file/144b6f1c334bc65acb6f4d64f04eef56.webp
    Icon🖼
      prompt
        [quality] 2D icon
        masterpiece of simplified art
        the foreground composition is centered and upscaled leaving no borders and no padding
        low detail
      negative
        photo
        doll
        anime
        cropped
        not centered
        big padding
        big border
        small scale
        small details
        collage
      url
        https://user.uploads.dev/file/42c906a086f3c5ee9b1e429fbc3c5bb6.webp
    Painting🎨
      prompt
        photorealistic painting
        the artist uses visible brushstrokes and subtle shading to achieve semi-realistic, slightly painterly effect, blending realism with illustrative qualities
        forms and surfaces carry a refined, painterly touch without losing a photographic feel
      negative
        3D-render, cgi, anime, photo
      url
        https://user.uploads.dev/file/2f5265c0140828c760ceee1b00025be3.webp
  resolution
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="resolution=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="resolution" ${item.getName==resolution?'checked':''} /><label>${'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    768x768
      https://user.uploads.dev/file/ee1ff561ffa4b338785585a7bb326021.webp
    512x768
      https://user.uploads.dev/file/69e7244349e1f42566df9f56f63cdd8d.webp
    512x512
      https://user.uploads.dev/file/e8c0cf737e69b29f85078ea14ea3de0d.webp
    768x512
      https://user.uploads.dev/file/af7899b7d6e02e2e9d467ed01d30abe3.webp
  filter
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="filter=this.value;" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="filter" ${item.getName==filter?'checked':item.getName=='<h3><b>filter</b></h3>'?'disabled':''} /><label>${item.getName}</label></div>`).join('')]
    Any filter
    <h3><b>filter</b></h3>
    black and white
    blue
      the image has a blue filter, with the blue colors being more saturated and the contrast being higher
    camera weather effects
      the camera lens is covered with [/day|sun/i.test(lighting)&&/any weather|clear/i.test(weather)?"sunflare":sceneWet?"raindrops":sceneCold?"{snowflakes|frost}":"{drops|dust|sand|smoke}"]
    extended depth-of-field
      the camera uses extended field-of-depth lens and f/22 aperture, and captures the scene from an angle that includes the surrounding [sceneVegetation?"trees and bushes":sceneOpenAir?"buildings, streets and trees":sceneTransportation?"seats and handrails":!sceneOpenAir&&!sceneWindowless&&!sceneDrawnCurtains?"space, view outside and the furniture":"space"], providing a sense of depth and [sceneOpenAir?"height":"spacious room"][actor=="Any actor"?"":" and the long distance between the viewer and the subject"]
      wide angle, everything in sharp focus, no bokeh, infinite depth of field
    fisheye
      the camera uses fisheye lens, the image is distorted and the edges are curved
    green
      the image has a green filter, with the green colors being more saturated and the contrast being higher
    grayscale
      the image is grayscale, in shades of gray
    monochrome
      the image is monochrome, with a single color
    old photo effect
      the image has characteristics of an old photo, such as faded colors, poor film quality, scratches, torn edges and stains.
    polaroid effect
      the image has characteristics of a polaroid photo, such as a white border and a slightly faded look
    polaryzing
      the image has a polarizing filter, with the colors being more saturated and the contrast being higher
      the reflections from liquids[actorType=="mechanical"?", metal":""] and other surfaces are reduced showing the depth to the material
    red
      the image has a red filter, with the red colors being more saturated and the contrast being higher
    sepia
      the image has sepia tones, giving it a warm, vintage look
    vignette
      the image has a vignette effect, with the edges of the image being darker than the center
    f/1.6 aperture
      cinematic camerawork with long focal length, shallow depth-of-field and aperture of f/1.6
      the foreground is blurred emphasizing depth and the distance to the target
    f/32 aperture
      the camera uses f/32 aperture, the image is sharp and the background is in focus
 //<=Style
toolsList // color, theme
  color
    Any #FFFFF1
    Aesthetic Blue #1F75FE
    Aesthetic Green #1CA350
    Aesthetic Red #B90000
    Aesthetic Yellow #F2E788
    Acid Blue #1F75FE
    Acid Green #B0BF1A
    Acid Red #B90000
    Acid Yellow #F2E788
    Active Blue #0D5BE1
    Active Green #6EC531
    Active Red #B90000
    Active Yellow #F2E788
    Algae Green #64AC27
    Alice Blue #F0F8FF
    Alizarin #E32636
    Alpine Green #5FA777
    Amaranth #E52B50
    Amazon Green #3B7A57
    Amber #FF7E00
    Amber Gold #FFBF00
    Amethyst #9966CC
    Antique Brass #CD9575
    Antique Bronze #665D1E
    Antique Fuchsia #915C83
    Antique Ruby #841B2D
    Antique White #FAEBD7
    Apple Green #8DB600
    Apricot #FBCEB1
    Aqua #00FFFF
    Aquamarine #7FFFD4
    Army Brown #827B60
    Army Green #4B5320
    Army Yellow #827B60
    Artichoke #8F9779
    Ash Gray #B2BEB5
    Asparagus #87A96B
    Atomic Tangerine #FF9966
    Auburn #A52A2A
    Aureolin #FDEE00
    Avocado Green #568203
    Attention Red #F42E17
    Avocado #568203
    Azure #007FFF
    Baby Blue #89CFF0
    Baby Pink #F4C2C2
    Baby Purple #CA9BF7
    Banana #FFE135
    Basic Blue #0D5BE1
    Basic Green #2DA815
    Basic Red #B80F0A
    Basic Yellow #F2E788
    Beige #F5F5DC
    Bisque #FFE4C4
    Bistre Brown #3D2B1F
    Bitter Lemon #CAE00D
    Bitter Lime #BFFF00
    Bittersweet #FE6F5E
    Black Bean #3D0C02
    Black Coral #54626F
    Black Leather #253529
    Black Olive #3B3C36
    Black Shadows #BFAFB2
    Blastoff Bronze #A57164
    Blizzard Blue #ACE5EE
    Blanched Almond #FFEBCD
    Black #000000
    Blond #FFE69E
    Blood Orange #D1001C
    Blood Red #660000
    Blue #0000FF
    Blue Bell #A2A2D0
    Blue Gray #6699CC
    Blue Green #0D98BA
    Blue Jeans #5DADEC
    Blue Violet #8A2BE2
    Bright Blue #0096FF
    Bright Green #66FF00
    Bright Mint #4FFFB0
    Bright Red #FF000D
    Bright Yellow #FFEA00
    Bronze #CD7F32
    Brown #8B4513
    Brown Sugar #AF6E4D
    British Racing Green #004225
    Brown #8B4513
    Buff #F0DC82
    Burgundy #800020
    Burlywood #DEB887
    Burnt Orange #CC5500
    Burnt Sienna #E97451
    Burnt Umber #8A3324
    Byzantine Purple #BD33A4
    Byzantium Purple #702963
    Cactus #5B6F55
    Cadet #536872
    Cadet Blue #5F9EA0
    Cadet Gray #91A3B0
    Cadmium Green #006B3C
    Cadmium Orange #ED872D
    Cadmium Red #E30022
    Cadmium Yellow #FFF600
    Cafe Noir #4B3621
    Cal Poly Green #1E4D2B
    Cambridge Blue #A3C1AD
    Camel #C19A6B
    Camouflage Green #78866B
    Canary Yellow #FFFF99
    Candy Apple Red #FF0800
    Candy Pink #E4717A
    Capri #00BFFF
    Caput Mortuum Brown #592720
    Caramel #AF6E4D
    Carbon Gray #625D5D
    Cardinal #C41E3A
    Caribbean Green #00CC99
    Caribbean Blue #1AC1DD
    Caribbean Red #CC0000
    Caribbean Yellow #F2E788
    Carmine #960018
    Carmine Pink #EB4C42
    Carnelian #B31B1B
    Carrot Orange #ED9121
    Casual Blue #0D5BE1
    Casual Green #0A6B0D
    Casual Red #AC1D1B
    Casual Yellow #F2E788
    Celadon #ACE1AF
    Celeste #B2FFFF
    Ceramic #FCFFF9
    Cerise #DE3163
    Cerise Pink #EC3B83
    Cerulean #007BA7
    Cerulean Blue #2A52BE
    Cetacean Blue #001440
    Champagne #F7E7CE
    Charcoal #36454F
    Chartreuse #7FFF00
    Chartreuse Yellow #DFFF00
    Cherry Red #D2042D
    Chestnut #954535
    Chili Red #E23D28
    Chinese Red #AA381E
    Chinese Violet #856088
    Chocolate #7B3F00
    Chrome Yellow #FFA700
    Cinereous #98817B
    Cinnamon #D2691E
    Citrine #E4D00A
    Citron #9FA91F
    Claret Red #7F1734
    Classic Blue #0D5BE1
    Classic Green #0A6B0D
    Classic Red #CF1827
    Classic Yellow #F2E788
    Cobalt Blue #0047AB
    Comfort Green #7AAD7B
    Cornflower Blue #6495ED
    Cornsilk #FFF8DC
    Cream #FFFDD0
    Crimson #DC143C
    Crimson Glory #BE0032
    Crimson Red #990000
    Cyan #00FFFF
    Dark Blue #00008B
    Dark Brown #654321
    Dark Carmine #841B2D
    Dark Cyan #008B8B
    Dark Gold #B8860B
    Dark gray #A9A9A9
    Dark Green #006400
    Dark Magenta #8B008B
    Dark Olive Green #556B2F
    Dark Orange #FF8C00
    Dark Orchid #9932CC
    Dark Red #8B0000
    Dark Salmon #E9967A
    Dark Scarlet #560319
    Dark Sea Green #8FBC8F
    Dark Slate Blue #483D8B
    Dark Slate Gray #2F4F4F
    Dark Tan #988558
    Dark Yellow #8B8000
    Dark yellow green #618822
    Deep Blue #0D5BE1
    Deep Brown #654321
    Deep Carmine #A9203E
    Deep Cerise #DA3287
    Deep Chestnut #B94E48
    Deep Cyan #008B8B
    Deep Fuchsia #C154C1
    Deep Gold #B8860B
    Deep Green #056608
    Deep Pink #FF1493
    Deep Red #850101
    Deep Sky Blue #00BFFF
    Deep Yellow #F2E788
    Denim #6F8FAF
    Denim Blue #1560BD
    Desert Sand #EDC9AF
    Diamond #B9F2FF
    Dijon #C49102
    Dim Gray #696969
    Dirt #9B7653
    Dirty Blond #D1C9AB
    Dirty Brown #B5651D
    Dirty Gray #A8A8A8
    Dirty Green #667C3E
    Dirty Red #B80F0A
    Dirty White #E8E4C9
    Dirty Yellow #F2E788
    Dodger Blue #1E90FF
    Dollar Bill Green #85BB65
    Drab #967117
    Duke Blue #00009C
    Dull Blue #8B9FEC
    Dull Green #7A9A7B
    Dull Red #B80F0A
    Dull Yellow #D1B606
    Dusty Blue #6699CC
    Dusty Green #8A9A5B
    Dusty Pink #D58A94
    Dusty Red #B80F0A
    Dusty Rose #C9A9A6
    Dusty Yellow #F2E788
    Earth Brown #654321
    Earth Green #5C6C3D
    Earth Red #B80F0A
    Earth Yellow #F2E788
    Ecru #C2B280
    Eggshell #F0EAD6
    Electric Blue #7DF9FF
    Electric Yellow #FFFF33
    Elegant Blue #19437D
    Elegant Green #0A6B0D
    Elegant Red #B80F0A
    Elegant Yellow #F2E788
    Emerald #50C878
    Emerald Green #5FBB9C
    Energy Blue #0D5BE1
    Energy Green #1CA350
    Energy Red #B80F0A
    Energy Yellow #F2E788
    Eton Blue #96C8A2
    Eucalyptus #44D7A8
    Faded Green #7BA05B
    Faded Blue #658CBB
    Faded Yellow #F2E788
    Fancy Blue #0D5BE1
    Fancy Green #0A6B0D
    Fancy Red #D10047
    Fancy Yellow #F2E788
    Fashion Blue #0D5BE1
    Fashion Green #0A6B0D
    Fashion Red #B80F0A
    Fire Red #E25822
    Firebrick #B22222
    Flame #E25822
    Flaming Red #F42E17
    Floral White #FFFAF0
    Fluorescent Blue #15F4EE
    Fluorescent Green #39FF14
    Foggy Gray #CBCAB6
    Forest #014421
    Forest Green #228B22
    Fresh Blue #318CE7
    Fresh Green #5EDC1F
    Fuchsia #FF00FF
    Gainsboro #DCDCDC
    Gamboge Orange Brown #E49B0F
    Generic Blue #0D5BE1
    Generic Green #0A6B0D
    Generic Red #B80F0A
    Generic Yellow #F2E788
    Gentle Blue #0D5BE1
    Gentle Green #0A6B0D
    Gentle Red #B80F0A
    Gentle Yellow #F2E788
    Genuine Blue #0D5BE1
    Genuine Green #0A6B
    Ghost White #F8F8FF
    Ginger #B06500
    Gingerbread #5E2C04
    Glamorous Blue #0D5BE1
    Glamorous Green #0A6B0D
    Glamorous Red #B80F0A
    Glamorous Yellow #F2E788
    Glossy Blue #0D5BE1
    Glossy Green #0A6B0D
    Glossy Red #DD0004
    Golden #FFD700
    Golden Brown #996515
    Golden Poppy #FCC200
    Golden Yellow #FFDF00
    Goldenrod #DAA520
    Grape #6F2DA8
    Grapefruit #FD5956
    Graphite #251607
    Grass #5DAE7B
    Grass Green #7CFC00
    Gray #808080
    Gray Asparagus #465945
    Gray Blue #6699CC
    Gray Green #5E716A
    Grayish Blue #5D89BA
    Grayish Green #8A9A5B
    Grayish Red #B80F0A
    Grayish Yellow #F2E788
    Green #00FF00
    Green Apple #8DB600
    Green Blue #0D98BA
    Green Gray #5E716A
    Green Yellow #ADFF2F
    Greenest Green #28B80F
    Han Blue #446CCF
    Han Purple #5218FA
    Harlequin #3FFF00
    Harvest Gold #DA9100
    Hazel #A0522D
    Heather #B7C3D0
    Heliotrope Violet #DF73FF
    Highlight Blue #0D5BE1
    Highlight Green #0A6B0D
    Highlight Red #B80F0A
    Highlight Yellow #F2E788
    Hollywood Cerise Pink #F400A1
    Honey #A98307
    Honeydew #F0FFF0
    Hot Pink #FF69B4
    Honeydew #F0FFF0
    Hot Magenta #FF1DCE
    Hot Pink #FF69B4
    Hunter Green #355E3B
    Ice Blue #99FFFF
    Iceberg Blue #71A6D2
    Icterine #FCF75E
    Illuminating Emerald #319177
    Imperial Blue #002395
    Imperial Purple #66023C
    Imperial Red #ED2939
    Independence #4C516D
    India Green #138808
    Indian Red #CD5C5C
    Indian Yellow #E3A857
    Indigo #4B0082
    Indian Red #CD5C5C
    Intense Red #C30913
    International Klein Blue #002FA7
    International Orange #FF4F00
    Iris #5A4FCF
    Irresistible Dirty Pink#B3446C
    Isabelline #F4F0EC
    Islamic Green #009
    Ivory #FFFFF0
    Jade #00A86B
    Jade Green #00A86B
    Japanese Indigo #264348
    Japanese Violet #5B3256
    Jasmine #F8DE7E
    Jasper #D73B3E
    Jazzberry Jam #A50B5E
    Jet #343434
    Jonquil #F4CA16
    June Bud #BDDA57
    Jungle Green #29AB87
    Kelly Green #4CBB17
    Khaki #C3B091
    Khaki Green #728639
    Kiwi Green #8EE53F
    Kobe Brown #882D17
    Kobi #E79FC4
    Kombu Green #354230
    Lava #CF1020
    Lavender #E6E6FA
    Lavender Blush #FFF0F5
    Lavender Gray #C4C3D0
    Lavender Indigo #9457EB
    Lavender Magenta #EE82EE
    Lavender Mist #E6E6FA
    Lavender Pink #FBAED2
    Lavender Purple #967BB6
    Lavender Rose #FBA0E3
    Lavender Violet #8A2BE2
    Lawn Green #7CFC00
    Leaf #71AA34
    Leaf Green #5CA904
    Lemon #FFF700
    Lemon Chiffon #FFFACD
    Lemon Curry #CCA01D
    Lemon Glacier #FDFF00
    Lemon Lime #E3FF00
    Lemon Meringue #F6EABE
    Lemon Yellow #FFF44F
    Licorice Deep Red #1A1110
    Liberty Violet #545AA7
    Light Blue #ADD8E6
    Light Brown #B5651D
    Light Coral #F08080
    Light Cyan #E0FFFF
    Light Goldenrod Yellow #FAFAD2
    Light gray #D3D3D3
    Light Green #90EE90
    Light Pink #FFB6C1
    Light Salmon #FFA07A
    Light Sea Green #20B2AA
    Light Sky Blue #87CEFA
    Light Slate Gray #778899
    Light Steel Blue #B0C4DE
    Light Yellow #FFFFE0
    Lime #BFFF00
    Lime Green #32CD32
    Linen #FAF0E6
    Lucky Green #0C9E5A
    Luminous Green #00B612
    Lush Green #00FF7F
    Luxury Red #B03737
    Magnetic Blue #142B6B
    Magneta #FF00FF
    Mahogany #C04000
    Maize #FBEC5D
    Majestic Blue #0D5BE1
    Majorelle Blue #6050DC
    Majorelle Green #ADFF2F
    Majorelle Red #B80F0A
    Majorelle Yellow #FFD700
    Malachite #0BDA51
    Mango #FF8243
    Marigold #EAA221
    Marine #042E60
    Marine Blue #01386A
    Marine Green #40E0D0
    Marker Green #9DAF00
    Marker Red #E11D3C
    Marker Yellow #F2E788
    Maroon #800000
    Matte Black #28282B
    Matte Blue #1D2951
    Matte Green #28382C
    Matte Dark Green #285D34
    Maximum Red #D92121
    Mellow Yellow #F8DE7E
    Melon #FEBAAD
    Medium Aquamarine #66CDAA
    Medium Blue #0000CD
    Medium Gray #BEBEBE
    Medium Orchid #BA55D3
    Medium Purple #9370DB
    Medium Sea Green #3CB371
    Medium Slate Blue #7B68EE
    Medium Spring Green #00FA9A
    Medium Turquoise #48D1CC
    Medium Violet Red #C71585
    Midnight Blue #191970
    Midnight Green #004953
    Military Green #4B5320
    Milk Chocolate #84563C
    Milk White #FDFFF5
    Mint Cream #F5FFFA
    Mint #3EB489
    Mint Green #98FF98
    Misty Rose #FFE4E1
    Mocha #967969
    Moccasin #FFE4B5
    Modern Blue #142B6B
    Modern Green #0A6B0D
    Modern Red #B80F0A
    Moonstone Blue #3AA8C1
    Moss Green #8A9A5B
    Muddy Green #657432
    Muddy Yellow #BFAC05
    Mulberry #C54B8C
    Mustard #FFDB58
    Natural Green #5CAE7B
    Natural Red #B80F0A
    Natural White #F2EFE6
    Nature Blue #4B89BF
    Navajo White #FFDEAD
    Navy Blue #000080
    Neon Green #39FF14
    Neon Blue #4D4DFF
    Neon Red #FF073A
    Neon Yellow #FFFF33
    Neon Pink #FF6EC7
    Neon Purple #9D00FF
    Neon Orange #FF5F1F
    Neon Cyan #00FEFC
    Neon Brown #A52A2A
    Neon Gold #FFD700
    Neon Bronze #CD7F32
    Neon Copper #B87333
    Neon Brass #B5A642
    Neon Nickel #727472
    Neon Zinc #7A7A7
    Ocean Blue #005F7F
    Ocean Green #48BF91
    Ochre #CC7722
    Old Blue #445B89
    Old Burgundy #43302E
    Old Copper #724A2F
    Old Gold #CFB53B
    Old Gray #8B8680
    Old Green #58804D
    Old Lace #FDF5E6
    Old Lavender #796878
    Old Lime #AFCB80
    Old Mauve #673147
    Old Moss Green #867E36
    Old Pink #C08081
    Old Rose #C08081
    Old Silver #848482
    Old Violet #8A2BE2
    Old White #F8F6F0
    Old Yellow #F0E68C
    Olive #808000
    Olive Green #B5B35C
    Olive Drab #6B8E23
    Onyx #353839
    Opal #A8C3BC
    Orange #FFA500
    Orchid #DA70D6
    Pale Blue #AFEEEE
    Pale Brown #987654
    Pale Carmine #AF4035
    Pale Cerulean #9BC4E2
    Pale Chestnut #DDADAF
    Pale Cornflower Blue #ABCDEF
    Pale Cyan #87D3F8
    Pale Gold #E6BE8A
    Pale Goldenrod #EEE8AA
    Pale Green #98FB98
    Pale Lavender #DCD0FF
    Pale Magenta #F984E5
    Pale Pink #FADADD
    Pale Plum #DDA0DD
    Pale Red #DB7093
    Pale Yellow #FFFF99
    Papaya Whip #FFEFD5
    Parrot Green #5CAE7B
    Pastel Blue #A7C7E7
    Pastel Brown #836953
    Pastel Coral #FF7F50
    Pastel Cyan #A2DDF0
    Pastel Gray #CFCFC4
    Pastel Green #77DD77
    Pastel Indigo #C3B1E1
    Pastel Lavender #DCD0FF
    Pastel Lime #BFFF00
    Pastel Magenta #F49AC2
    Pastel Maroon #800000
    Pastel Navy #000080
    Pastel Olive #BAB86C
    Pastel Orange #FFB347
    Pastel Pink #FFD1DC
    Pastel Purple #B39EB5
    Pastel Teal #99C5C4
    Pastel Red #FF6961
    Pastel Rose #FFE4E1
    Pastel Salmon #FFA07A
    Pastel Sea Green #9FE2BF
    Pastel Sky Blue #A2DDF0
    Pastel Tan #D1B26F
    Pastel Turquoise #99C5C4
    Pastel Violet #CB99C9
    Pastel Yellow #FDFD96
    Pastel Yellow Green #C5E17A
    Peach #FFE5B4
    Peach Orange #FFCC99
    Peach Puff #FFDAB9
    Pear #D1E231
    Pearl #EAE0C8
    Pearl White #F8F6F0
    Perfection Blue #0D5BE1
    Perfect Blue #045FD0
    Perfect Green #0A6B0D
    Perfect Red #B80F0A
    Peridot #E6E200
    Periwinkle #CCCCFF
    Persian Blue #1C39BB
    Persian Green #00A693
    Persian Indigo #32127A
    Persian Orange #D99058
    Persian Pink #F77FBE
    Persian Plum #701C1C
    Persian Red #CC3333
    Persian Rose #FE28A2
    Persian Violet #8C8C8C
    Phthalo Blue #000F89
    Phthalo Green #123524
    Pigment Green #00A550
    Pine Green #01796F
    Pineapple #FEE12B
    Pink #FFC0CB
    Pink Red #F400A1
    Pistachio #93C572
    Platinum #E5E4E2
    Plum #DDA0DD
    Pollen #F4C430
    Powder Blue #B0E0E6
    Premium Blue #0D5BE1
    Premium Green #146321
    Prussian Blue #003153
    Puce #CC8899
    Pumpkin #FF7518
    Pure Blue #0000FF
    Pure Green #00B612
    Pure Red #B80F0A
    Purple #800080
    Purple Heart #69359C
    Purple Navy #4E5180
    Purple Red #990066
    Purple Taupe #50404D
    Quartz #51484F
    Racing Blue #1E1E66
    Racing Green #004225
    Racing Red #B80F0A
    Raspberry #E30B5C
    Raw Sienna #D68A59
    Raw Umber #826644
    Real Blue #0D5BE1
    Real Green #0A6B0D
    Real Red #B80F0A
    Rebecca Purple #663399
    Red Brown #A52A2A
    Red #FF0000
    Red Devil #860111
    Reddish #C44240
    Red Glow #D44A47
    Redhead #E1621D
    Red Hot #F42E17
    Red Orange #FF5349
    Red Pink #E3256B
    Red Party #CC3F4D
    Red Purple #953553
    Red Rose #C21E56
    Red Velvet #7B3539
    Red Wine #722F37
    Redwood #A45A52
    Relaxing Green #92D293
    Renaissance Blue #0D5BE1
    Rich Blue #0D5BE1
    Rich Green #1A4314
    Rich Orange #FF7F00
    Rich Red #E11218
    Rich Violet #6A0DAD
    Rich Yellow #FFD700
    Robin Egg Blue #00CCCC
    Rock Blue #0D5BE1
    Rose #FF007F
    Rose Gold #B76E79
    Rose Pink #FF66CC
    Rose Red #C21E56
    Rose Taupe #905D5D
    Rosewood #65000B
    Romantic Blue #AAD1E7
    Romantic Green #92D293
    Romantic Red #BD2734
    Romantic Rose #C21E56
    Rosy Brown #BC8F8F
    Royal #0D5BE1
    Royal Blue #4169E1
    Royal Green #0A6B0D
    Royal Carmine #960018
    Royal Red #B80F0A
    Royal Purple #7851A9
    Ruby #E0115F
    Russet #80461B
    Rust #B7410E
    Rustic Red #B80F0A
    Saffron #F4C430
    Safety Orange #FF6600
    Sage Green #9CAF88
    Salmon #FA8072
    Salmon Pink #FF91A4
    Sand #C2B280
    Sand Dune #967117
    Sandy Brown #F4A460
    Sangria #92000A
    Sapphire #0F52BA
    Satin #8A2BE2
    Satin Gold #C5A560
    Satin Green #0A6B0D
    Satin Red #B80F0A
    Saturated Blue #0D5BE1
    Saturated Green #0A6B0D
    Saturated Red #B80F0A
    Scarlet #FF2400
    School Bus Yellow #FFD800
    Sea Blue #006994
    Sea Foam #93E9BE
    Sea Green #2E8B57
    Seashell #FFF5EE
    Seaweed #4BC7CF
    Selective Yellow #FFBA00
    Sepia #704214
    Shamrock Green #009E60
    Shiny Blue #0D5BE1
    Shiny Green #59CA4E
    Shiny Red #B80F0A
    Sienna #A0522D
    Silver #C0C0C0
    Simple Blue #0D5BE1
    Simple Green #0A6B0D
    Simple Red #B80F0A
    Sky Blue #87CEEB
    Slate Blue #6A5ACD
    Slate Gray #708090
    Smoke #738276
    Snow #FFFAFA
    Soft Blue #A2DDF0
    Soft Green #C1E1C1
    Soft Red #FFCCCB
    Soft White #F2EFE6
    Solid Green #00B612
    Solid Blue #2664F5
    Solid Red #B80F0A
    Space Blue #1D2951
    Space Gray #343D52
    Space Green #0A6B0D
    Space Red #B80F0A
    Spanish Blue #0070BB
    Spanish Green #009150
    Spanish Red #E60026
    Spanish Yellow #F6B600
    Spicy Red #B80F0A
    Spring Bud #A7FC00
    Spring Green #00FF7F
    Steel #B0C4DE
    Steel Blue #4682B4
    Straw #E4D96F
    Strong Red #EF0307
    Subtle Blue #A2DDF0
    Subtle Green #C1E1C1
    Subtle Red #FFCCCB
    Subtle White #F2EFE6
    Summer Green #5CAE7B
    Sun #FDB813
    Sunflower #FFC512
    Sunny #F2E788
    Sunlight #FADF98
    Sunset #FAD6A5
    Sunset Orange #FD5E53
    Sunset Red #B80F0A
    Sunset Yellow #FAD6A5
    Super Blue #0D5BE1
    Super Green #0A6B0D
    Super Red #B80F0A
    Sweet Blue #A2DDF0
    Sweet Green #C1E1C1
    Sweet Red #FFCCCB
    Sweet White #F2EFE6
    Synthetic Blue #142B6B
    Synthetic Green #0A6B0D
    Synthetic Red #B80F0A
    Tan #D2B48C
    Tangerine #F28500
    Tangerine Yellow #FFCC00
    Tango Red #B80F0A
    Tanzanite Blue #1967BE
    Taupe #483C32
    Taupe Gray #8B8589
    Tea Green #D0F0C0
    Teal #008080
    Teal Blue #367588
    Terracotta #E2725B
    Thistle #D8BFD8
    Tiffany Blue #0ABAB5
    Tiger Orange #F96F00
    Timberwolf #DBD7D2
    Tomato #FF6347
    Tool Blue #0D5BE1
    Tool Green #0A6B0D
    Tool Red #B80F0A
    Topaz #FFC87C
    Toucan #FF6F52
    Touch Of Green #DBE9D5
    Traditional Blue #0D5BE1
    Traditional Green #0A6B0D
    Traditional Red #B80F0A
    Translucent Blue #0D5BE1
    Translucent Green #0A6B0D
    Translucent Red #B80F0A
    Transparent Blue #0D5BE1
    Transparent Green #0A6B0D
    Transparent Red #B80F0A
    Trendy Blue #0D5BE1
    Trendy Green #199619
    Trendy Red #B80F0A
    Tropical Blue #1E90FF
    Tropical Green #008B45
    Tropical Red #B80F0A
    Turquoise #40E0D0
    Turquoise Blue #00FFEF
    Turquoise Green #A0D6B4
    Twilight Blue #0D5BE1
    Twilight Green #0A6B0D
    Twilight Red #B80F0A
    Ultra Blue #0038A8
    Ultra Green #0A6B0D
    Ultra Red #B80F0A
    Ultramarine #3F00FF
    Ultramarine Blue #4166F5
    Umber #635147
    Unique Blue #0D5BE1
    Unique Green #0A6B0D
    Unique Red #B80F0A
    Universal Blue #0D5BE1
    Universal Green #0A6B0D
    Universal Red #B80F0A
    Unreal Blue #0D5BE1
    Unreal Green #0A6B0D
    Unreal Red #B80F0A
    Up Blue #0D5BE1
    Up Green #0A6B0D
    Up Red #B80F0A
    Van Dyke Brown #664228
    Vanilla #F3E5AB
    Vegas Gold #C5B358
    Velvet #800080
    Venetian Red #C80815
    Verdigris Teal #43B3AE
    Vermilion #E34234
    Verdant Green #127D4A
    Vibrant Green #00FF00
    Vibrant Blue #0022EE
    Vibrant Red #FF000D
    Vintage Blue #303D57
    Vintage Green #367055
    Vintage Red #B80F0A
    Violet #EE82EE
    Violet Blue #324AB2
    Violet Eggplant #991199
    Violet Purple #8A2BE2
    Violet Red #F75394
    Violet Rose #F7468A
    Violet Tulip #B2A1D7
    Violet White #F2E6FF
    Violet Yellow #F0E68C
    Vivid Blue #0022EE
    Vivid Green #00FF00
    Vivid Red #F70D1A
    Warm Blue #0D5BE1
    Warm Green #4B5320
    Warm Red #B80F0A
    Water Blue #005F7F
    Water Green #48BF91
    Watermelon #FC6C85
    Watermelon Red #B80F0A
    Watermelon Pink #FF6F52
    Watermelon Yellow #FAD6A5
    Watery Blue #A2DDF0
    Watery Green #C1E1C1
    Watery Red #FFCCCB
    Watery White #F2EFE6
    Wave Blue #0D5BE1
    Wave Green #0A6B0D
    Wave Red #B80F0A
    Wedgewood Blue #4F7BA7
    Wedgewood Green #0A6B0D
    Wedgewood Red #B80F0A
    Wheat #F5DEB3
    White #FFFFFF
    Whisper White #F2EFE6
    White Chocolate #EDE6D6
    White Lilac #F8F8FF
    White Pearl #F8F6F0
    White Smoke #F5F5F5
    Wild Blue #0D5BE1
    Wild Green #0A6B0D
    Wild Red #B80F0A
    Wild Strawberry #FF43A4
    Wild Watermelon #FC6C85
    Wine #722F37
    Wine Red #B80F0A
    Winter Blue #0D5BE1
    Winter Green #0A6B0D
    Winter Red #B80F0A
    Wisteria #C9A0DC
    Wood #966F33
    Wood Brown #C19A6B
    Wood Green #4B5320
    Wood Red #B80F0A
    Wood Violet #8A2BE2
    Wood White #F2EFE6
    Wood Yellow #F0E68C
    Xanadu #738678
    Xanthic #EEED09
    Xanthous #F1B42F
    Yacht Blue #0D5BE1
    Yacht Green #0A6B0D
    Yacht Red #B80F0A
    Yale Blue #0F4D92
    Yale Green #0A6B
    Yellow #FFFF00
    Yellow Green #9ACD32
    Yellow Orange #FFAE42
    Yellow Rose #FFF000
    Yellow Sun #FDB813
    Yellow Tan #F0E68C
    Yellow White #FFFFE0
    Yellowish #F0E68C
    Yellowish Green #9ACD32
    Yellowish Orange #FFAE42
    Yellowish Tan #F0E68C
    Young Blue #0D5BE1
    Young Green #5EDC1F
    Young Red #B80F0A
    Zaffre Purple #0014A8
    Zinnwaldite #EBC2AF
    Zomp Teal #39A78E
    Zucchini #044022
  theme
    $output = [this.selectAll.map(item => `<div><input value="${item.getName}" onchange="theme=this.value;themeChoice();" type="radio" id="${item.getName.replaceAll(" ", "_")}" name="theme" ${item.getName==theme?'checked':''} /><label>${'<img src='+item.selectAll[0]+'>'}${item.getName}</label></div>`).join('')]
    Concrete Jungle //default
      https://user.uploads.dev/file/2a627363185ea7ef5bd7db74ad10f2e6.webp
    Chocolate Dream
      https://user.uploads.dev/file/b574af5809cb86af89f32eddd34f89fd.webp
    Generator PRO
      https://user.uploads.dev/file/a582456ca6804d699407d7c395c3d021.webp
    Sea journey
      https://user.uploads.dev/file/348b7487522998b87dd46aa370359efa.webp
 //<=Tools
//Helper functions
combine(sentenceArray)=>
  return sentenceArray.selectAll.filter(item => String(item).trim()!="").map((item,index,array) => String(item).slice(-1)==" "||index==array.length-1?item:item+", ").join("").replace(/,+/g, ',').replace(/ ,/g, ',').replace(/\s{2,}/g, ' ').replace(/[^a-zA-Z0-9\]\}]+$/, "");
