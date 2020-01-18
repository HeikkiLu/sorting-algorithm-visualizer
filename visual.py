import PySimpleGUIQt as sg
import random
import bubblesort, insertionsort, selectionsort


BAR_SPACING, BAR_WIDTH, EDGE_OFFSET = 11, 10, 3
DATA_SIZE = GRAPH_SIZE = (800,500) 

# Change theme
sg.theme_background_color('#8F90A0')


# This function draws the bars to graph
def draw_bars(graph, items):
    for i, item in enumerate(items):
        graph.DrawRectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, item),
                            bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color='#B56089')

def main():
    # List to sort
    num_bars = DATA_SIZE[0] // (BAR_WIDTH+1)
    arr = [DATA_SIZE[1]//num_bars*i for i in range(1, num_bars)]

    # Window layout
    graph = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE, background_color='#F5F6F4')
    layout = [[sg.Text('Visualization', size=(30, 1), font=("Helvetica", 25), background_color='#8F90A0', text_color='#FFFFFF')], 
            [graph],
            [sg.Button('Select sorting method', button_color=['#FFFFFF','#35343B'], font=("Helvetica", 12)), sg.Button('Generate new array', button_color=['#FFFFFF','#35343B'], font=("Helvetica", 12))]]
            

    window = sg.Window('Algorithm Visualizer', layout)
    window.Finalize()

    draw_bars(graph, arr)
    
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break

        if event == 'Generate new array':
            graph.Erase()
            random.shuffle(arr)
            draw_bars(graph, arr)

        if event == 'Select sorting method':
            l2 = [[sg.T('Choose sorting method', font=("Helvetica", 12), background_color='#8F90A0', text_color='#FFFFFF')],
            [sg.Listbox(['Bubble', 'Insertion', 'Selection'], size=(16,3))],
            [sg.Ok()]]
            w2 = sg.Window('Choose sorting method', l2)
            button, values = w2()
            w2.close()
            try:
                if values[0][0] == 'Bubble':
                    sort = bubblesort.bubbleSort(arr)
                    sortmethod = 'Bubble'

                elif values[0][0] == 'Insertion':
                    sort = insertionsort.insertionSort(arr)
                    sortmethod = 'Insertion'

                else:
                    sort = selectionsort.selectionSort(arr)
                    sortmethod = 'Selection'
            except:
                sg.Popup('None selected.', font=("Helvetica", 12), background_color='#8F90A0', text_color='#FFFFFF')
                continue

            timeout=10

            for partially_sorted_list in sort:
                event, values = window.read(timeout=timeout)
                if event is None:
                    break
                graph.Erase()
                draw_bars(graph, partially_sorted_list)
                timeout = int(10)
            sg.Popup(f'{sortmethod} sort done.', font=("Helvetica", 12), background_color='#8F90A0', text_color='#FFFFFF')
        
            



if __name__ == "__main__":
    main()