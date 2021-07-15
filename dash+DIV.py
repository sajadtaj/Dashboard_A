import dash
import dash_html_components as html
import dash_html_components as dcc
import dash_bootstrap_components as dbc
#-------------------------------------------------------------------------------
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
#-------------------------------------------------------------------------------
#           component of dashboard Box
#-------------------------------------------------------------------------------
component_slider=html.H2('Slider')
component_1=html.H2('Box Number 1')
component_2=html.H2('Box Number 2')
component_3=html.H2('Box Number 3')
component_4=html.H2('Box Number 4')
component_5=html.H2('Box Number 5')
component_6=html.H2('Box Number 6')
component_7=html.H2('Box Number 7')
component_8=html.H2('Box Number 8')
component_9=html.H2('Box Number 9')


#------------------------------------------------------------------------------
app =dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
layer_1=html.Div([
    html.Div(
        children=[component_slider],
        style={'width':'10%',
                'border-style': 'solid',
                'border-color':'#280B6F',
                'border-width':' 1px',
                #'border-top-style': 'dotted',
                'border-top-left-radius': '1px',
                'border-bottom-left-radius': '1px', #  or border-radius: 22px 45px 30px 10px;

                #'padding':'10px 10px 10px 10px',
                'backgroundColor': '#6730EC',
                'textAlign': 'center',
                'display': 'inline-block',
                'height':'50rem'
                },
            ),
    html.Div(
        children=[
            html.Div(
                [
                html.Div([component_1],style={'width':'98%','height':'23rem' ,'backgroundColor': '#ffffff','border-color':'#D2F6FC','border-radius':'10px' ,'margin':'10px','border-style': 'solid','display': 'inline-block',}),
                html.Div([component_2],style={'width':'98%','height':'23rem' ,'backgroundColor': '#ffffff','border-color':'#D2F6FC','border-radius':'10px' ,'margin':'10px','border-style': 'solid', 'display': 'inline-block'}),
                ],style={'width':'60%',
                        #'padding':'10px 10px 10px 10px',
                        'backgroundColor': '#D8E3E9',
                        'textAlign': 'center',
                        'display': 'inline-block',
                        'height':'50rem'
                        },
            ),
            html.Div(
                [
                html.Div([component_3],style={'width':'95%','border-color':'#D2F6FC','border-radius':'10px' ,'margin':'5px','border-style': 'solid','backgroundColor': '#ffffff','height':'13rem','display': 'inline-block', }),
                html.Div([component_4],style={'width':'95%','border-color':'#D2F6FC','border-radius':'10px' ,'border-style': 'solid','backgroundColor': '#ffffff','height':'22rem','display': 'inline-block', }),
                html.Div([component_5],style={'width':'95%','border-color':'#D2F6FC','border-radius':'10px' ,'margin':'5px','border-style': 'solid','backgroundColor': '#ffffff','height':'13rem','display': 'inline-block', }),
                ],style={'width':'20%',
                        #'padding':'10px 10px 10px 10px',
                        'backgroundColor': '#D8E3E9',
                        'textAlign': 'center',
                        'display': 'inline-block',
                        'height':'50rem'
                        },
            ),
            html.Div(
                [
                html.Div([component_6],style={'width':'100%','height':'12.5rem','display': 'inline-block','backgroundColor': '#BA49F0'}),
                html.Div([component_7],style={'width':'100%','height':'12.5rem','display': 'inline-block','backgroundColor': '#E8236F'}),
                html.Div([component_8],style={'width':'100%','height':'12.5rem','display': 'inline-block','backgroundColor': '#FFD644'}),
                html.Div([component_9],style={'width':'100%','height':'12.5rem','display': 'inline-block','backgroundColor': '#0085FF'}),
                ],style={'width':'20%',
                        #'padding':'10px 10px 10px 10px',
                        'backgroundColor': '#D8E3E9',
                        'textAlign': 'center',
                        'display': 'inline-block',
                        'height':'50rem'
                        },

            ),
        ],
        style={'display': 'flex',
                'backgroundColor': '#112211',
                'height':'50rem',
                'width':'90%'
                }
    ),
],style={'display': 'flex' }
)





app.layout=html.Div(
    children=[
    layer_1
    ]
)
if __name__ == '__main__':
    app.run_server(debug=True , port=2019)
