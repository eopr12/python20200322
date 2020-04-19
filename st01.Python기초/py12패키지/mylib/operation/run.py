from mylib.sound.echo import echo_test  # ..-->부모폴더의


def render_test():
    result = None
    
    try:
        print("render")
        echo_test()
    except Exception as ex:
        pass
    

    echo_test()

if __name__ == "__main__":
    render_test()
