import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import  pandas as pd
import plotly.graph_objects as go
#------------------------------------------------------------------DATA-------
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
df_1 =  pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",dtype={"fips": str})
df_2 = px.data.medals_long()
#-------------------------------------------------------------------------------
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
#-------------------------------------------------------------------------------
#          figure
#-------------------------------------------------------------------------------
fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)
fig_1 = px.choropleth(locations=["CA", "TX", "NY"], locationmode="USA-states", color=[1,2,3], scope="usa")
fig_2 = px.bar(df_2, x="nation", y="count", color="medal", title="Long-Form Input")

#-------------------------------------------------------------------------------
#           component of dashboard Box
#-------------------------------------------------------------------------------
component_slider=dbc.Card(
    [
        dbc.CardHeader("Slider"),
        dbc.CardBody(
            [
                html.H4("slider title", className="card-title"),
                html.P("describe your perfect date", className="card-text"),
                html.Br(),
                dbc.Nav(
                    [
                    dbc.NavLink("Nav Link 1", href="/"      , active="exact"),
                    dbc.NavLink("Nav link 2", href="/page-1", active="exact"),
                    dbc.NavLink("Nav Link 2", href="/page-2", active="exact"),
                    ],
                    vertical=True,
                    pills=True,
                )
            ]
        ),
        dbc.CardFooter("designed By Sajad Taj"),
    ],
    style={"width": "100%",'height':'50rem', 'text-color':'#0E3854'},
    color="#F9F1F0",

)
component_1= dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
component_2= dcc.Graph(
        id='fertaliyt rate',
        figure=fig_1
    )
component_3=dcc.Graph(
        id='bar chart',
        figure=fig_2
    )
component_4=dbc.Card(
    dbc.ListGroup(
        [
        dbc.ListGroupItem("The primary item", color="primary"),
        dbc.ListGroupItem("A secondary item", color="secondary"),
        dbc.ListGroupItem("A successful item", color="success"),
        dbc.ListGroupItem("A warning item", color="warning"),
        dbc.ListGroupItem("A dangerous item", color="danger"),
        dbc.ListGroupItem("An informative item", color="info"),
        ],
        flush=True,

    ),
    style={"width": "100%", 'height':'14rem'},
)
#component_5=html.H2('Box 5')
component_6=dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "100%"},
    color="info"
)
component_7=dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "100%"},
    color="danger"
)
component_8=dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "100%"},
    color="warning"
)
component_9=dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "100%"},
    color="success"
)


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
                html.Div([component_3],style={'width':'95%','border-color':'#D2F6FC','border-radius':'10px' ,'border-style': 'solid','backgroundColor': '#ffffff','height':'30rem','display': 'inline-block', }),
                html.Div([component_4],style={'width':'95%','border-color':'#D2F6FC','border-radius':'10px' ,'border-style': 'solid','backgroundColor': '#ffffff','height':'20rem','display': 'inline-block', }),
                #html.Div([component_5],style={'width':'95%','border-color':'#D2F6FC','border-radius':'10px' ,'margin':'5px','border-style': 'solid','backgroundColor': '#ffffff','height':'0rem','display': 'inline-block', }),
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
