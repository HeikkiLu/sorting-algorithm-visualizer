import PySimpleGUIQt as sg
import random
import bubblesort, insertionsort, selectionsort

BAR_SPACING, BAR_WIDTH, EDGE_OFFSET = 11, 10, 3
DATA_SIZE = GRAPH_SIZE = (800,500) 

def draw_bars(graph, items):
    for i, item in enumerate(items):
        graph.DrawRectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, item),
                            bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0), fill_color='#76506d')


def main():
    sg.theme('DarkBlue1')
    # List to sort
    num_bars = DATA_SIZE[0] // (BAR_WIDTH+1)
    arr = [DATA_SIZE[1]//num_bars*i for i in range(1, num_bars)]
    random.shuffle(arr)

    # Window layout
    graph = sg.Graph(GRAPH_SIZE, (0,0), DATA_SIZE)
    layout = [[graph]]

    window = sg.Window('Algorithm Visualizer', layout)
    window.Finalize()

    draw_bars(graph, arr)
    
    l2 = [[sg.T('Choose sorting method')],
          [sg.Listbox(['Bubble', 'Insert', 'Selection'], size=(12,3))],
          [sg.Ok()],]
    w2 = sg.Window('Choose sorting method', l2)
    button, values = w2()
    w2.close()

    if values[0][0] == 'Bubble':
        sort = bubblesort.bubbleSort(arr)
    elif values[0][0] == 'Insertion':
        sort = insertionsort.insertionSort(arr)
    else:
        sort = selectionsort.selectionSort(arr)

    timeout=10

    for partially_sorted_list in sort:
        event, values = window.read(timeout=timeout)
        if event is None:
            break
        graph.Erase()
        draw_bars(graph, partially_sorted_list)
        timeout = int(10)
    sg.Popup('Sorting done.')

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break

if __name__ == "__main__":
    main()

