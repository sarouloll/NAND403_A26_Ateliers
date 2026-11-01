from maya import cmds

selectionList = cmds.ls (selection=True, type='transform')

startFrame = cmds.playbackOptions(query=True, minTime=True)
endFrame = cmds.playbackOptions(query=True, maxTime=True)


for pCube1 in selectionList:
    cmds.setKeyframe(pCube1, time=startFrame, attribute='translateZ', value = 0 )
    cmds.setKeyframe(pCube1, time=startFrame, attribute='translateX', value = 0 )

    cmds.setKeyframe(pCube1, time=startFrame + 10, attribute='translateZ', value=25)
    cmds.setKeyframe(pCube1, time=startFrame + 10, attribute='translateX', value=50)

    cmds.setKeyframe(pCube1, time=startFrame + 40, attribute='translateZ', value=50)
    cmds.setKeyframe(pCube1, time=startFrame + 60, attribute='translateX', value=75)
   
    cmds.setKeyframe(pCube1, time=endFrame, attribute='translateZ', value = 100 )
    cmds.setKeyframe(pCube1, time=endFrame, attribute='translateX', value = 0 )
 
