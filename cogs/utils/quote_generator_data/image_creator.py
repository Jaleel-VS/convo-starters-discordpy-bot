from os import path
import imgkit

dir_path = path.dirname(path.dirname(path.realpath(__file__)))


def create_image(user_name, user_avatar, message_content):
    options = {
        'format': 'png',
        'crop-w': '637',
        'encoding': "UTF-8",
    }

    font_size = ""

    font_sizes = {
        60: 'x-large',
        100: 'large',
        150: 'small',
    }

    for fs in font_sizes.keys():
        if len(message_content) <= fs:
            font_size = font_sizes[fs]
            break

    html = f'''
            <html>
            <head>
            <style>
                .myImage {{
            float: left;
            -webkit-filter: grayscale(100%); /* Safari 6.0 - 9.0 */
            filter: grayscale(100%);
            border: 2px solid white;
            border-right: 0;
            }}


            .quote {{
                float: left;
                width: 376px;
                height: 256px;
                margin-top: 0;
                margin-bottom: 0;
                background-color: #0c0c0c;
                border: 2px solid white;
                border-left: 0;

                text-align: center;
                }}

            .main-quote {{
            color: white;
            font-family: sans-serif;
            font-size: {font_size};
            font-style: italic;
            padding: 10% 5% 5%;
            }}

            .author {{
                color: white;
                font-size: larger;
                font-family: cursive;
            }}

            span:after,
        span:before{{
            content:"\\00a0\\00a0\\00a0\\00a0\\00a0";
            text-decoration:line-through;
        }}

        body {{
            padding: 0;
            margin: 0;
        }}
            </style>
            </head>
                <img src="{user_avatar}" class="myImage"/>
                <div class="quote">
                    <p class="main-quote">{message_content}</p>
                    <p class="author"><span> {user_name} </span></p>
                </div>
            </html>
        '''

    css = f'''
    .myImage {{
        float: left;
        -webkit-filter: grayscale(100%); /* Safari 6.0 - 9.0 */
        filter: grayscale(100%);
        border: 2px solid white;
        border-right: 0;
        }}


        .quote {{
            float: left;
            width: 376px;
            height: 256px;
            margin-top: 0;
            margin-bottom: 0;
            background-color: #0c0c0c;
            border: 2px solid white;
            border-left: 0;

            text-align: center;
            }}

        .main-quote {{
        color: white;
        font-family: sans-serif;
        font-size: {font_size};
        font-style: italic;
        padding: 10% 5% 5%;
        }}

        .author {{
            color: white;
            font-size: large;
            font-family: Cursive;
        }}

        span:after,
    span:before{{
        content:"\\00a0\\00a0\\00a0\\00a0\\00a0";
        text-decoration:line-through;
    }}

    body {{
        padding: 0;
        margin: 0;
    }}

    '''
    img_path = f"{dir_path}/quote_generator_data/picture.png"
    imgkit.from_string(html, img_path, options=options)
    return img_path
