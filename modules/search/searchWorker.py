from modules.search.Search import Search


def searchWorker(pause, pipelineIn, pipelineOut):
  
    print("Start Search")
    
    search = Search()    
    
    pause.acquire()
    pause.release()

    values = pipelineIn.get()

    
