import React, {StyleSheet, Dimensions, PixelRatio} from "react-native";
const {width, height, scale} = Dimensions.get("window"),
    vw = width / 100,
    vh = height / 100,
    vmin = Math.min(vw, vh),
    vmax = Math.max(vw, vh);

export default StyleSheet.create({
    "inbox-box": {
        "maxHeight": 550,
        "minHeight": 550,
        "overflowX": "hidden",
        "overflowY": "scroll",
        "width": "100%"
    },
    "u-pf-up": {
        "maxWidth": "100%",
        "paddingTop": 15,
        "paddingRight": 0,
        "paddingBottom": 15,
        "paddingLeft": 0
    },
    "u-pf-pic": {
        "position": "relative"
    },
    "u-pf-pic:hover divu-pf-pic-edit": {
        "display": "inline-block"
    },
    "u-pf-pic-edit": {
        "fontWeight": "600",
        "position": "absolute",
        "height": 35,
        "width": "100%",
        "bottom": 0,
        "background": "rgba(0, 0, 0, 0.5)",
        "display": "none",
        "paddingTop": 9
    },
    "f_upload": {
        "minHeight": 45,
        "boxShadow": "0 0 0 0 !important"
    },
    "btn-center-text": {
        "fontFamily": "'open_sansbold'",
        "border": "1px solid #eee9e9",
        "marginTop": 20,
        "marginRight": 0,
        "marginBottom": 0,
        "marginLeft": 0,
        "display": "inline-block",
        "paddingTop": 10,
        "paddingRight": 0,
        "paddingBottom": 10,
        "paddingLeft": 0,
        "background": "#ffffff",
        "width": "100%",
        "textAlign": "center"
    },
    "btn-gray": {
        "backgroundColor": "#8c8e86",
        "color": "#FFFFFF",
        "fontWeight": "bold",
        "paddingTop": 5,
        "paddingRight": 15,
        "paddingBottom": 5,
        "paddingLeft": 15
    },
    "btn-gray:hover": {
        "backgroundColor": "#a1a596",
        "color": "#FFFFFF",
        "fontWeight": "bold"
    },
    "btn-s-green": {
        "backgroundColor": "#95c809",
        "color": "#FFFFFF",
        "fontWeight": "bold",
        "paddingTop": 5,
        "paddingRight": 15,
        "paddingBottom": 5,
        "paddingLeft": 15
    },
    "btn-green": {
        "backgroundColor": "#95c809",
        "color": "#FFFFFF",
        "fontWeight": "bold",
        "paddingTop": 5,
        "paddingRight": 15,
        "paddingBottom": 5,
        "paddingLeft": 15
    },
    "btn-s-green:hover": {
        "backgroundColor": "#A4DC0A",
        "color": "#FFFFFF",
        "fontWeight": "bold",
        "paddingTop": 5,
        "paddingRight": 15,
        "paddingBottom": 5,
        "paddingLeft": 15
    },
    "btn-green:hover": {
        "backgroundColor": "#A4DC0A",
        "color": "#FFFFFF",
        "fontWeight": "bold"
    },
    "btn-s-blue": {
        "backgroundColor": "#011257",
        "color": "#FFFFFF",
        "fontWeight": "bold",
        "paddingTop": 5,
        "paddingRight": 15,
        "paddingBottom": 5,
        "paddingLeft": 15
    },
    "btn-blue": {
        "backgroundColor": "#011257",
        "color": "#FFFFFF",
        "fontWeight": "bold",
        "paddingTop": 5,
        "paddingRight": 15,
        "paddingBottom": 5,
        "paddingLeft": 15
    },
    "btn-s-blue:hover": {
        "backgroundColor": "#01197A",
        "color": "#FFFFFF",
        "fontWeight": "bold",
        "paddingTop": 5,
        "paddingRight": 15,
        "paddingBottom": 5,
        "paddingLeft": 15
    },
    "btn-blue:hover": {
        "backgroundColor": "#01197A",
        "color": "#FFFFFF",
        "fontWeight": "bold"
    },
    "form-group > button": {
        "borderRadius": 0,
        "minHeight": 30,
        "border": 0
    },
    "form-group > a": {
        "borderRadius": 0,
        "border": 0,
        "minHeight": 30
    },
    "form-group > input": {
        "borderRadius": 0,
        "minHeight": 30
    },
    "form-group > textarea": {
        "borderRadius": 0
    },
    "m-l-5": {
        "marginLeft": 5
    },
    "m-r-5": {
        "marginRight": 5
    },
    "m-b-5": {
        "marginBottom": 5
    },
    "m-t-5": {
        "marginTop": 5
    },
    "m-l-10": {
        "marginLeft": 10
    },
    "m-r-10": {
        "marginRight": 10
    },
    "m-b-10": {
        "marginBottom": 10
    },
    "m-t-10": {
        "marginTop": 10
    },
    "m-l-15": {
        "marginLeft": 15
    },
    "m-r-15": {
        "marginRight": 15
    },
    "m-b-15": {
        "marginBottom": 15
    },
    "m-t-15": {
        "marginTop": 15
    },
    "m-t-50": {
        "marginTop": 50
    },
    "m-b-50": {
        "marginBottom": 50
    },
    "p-0": {
        "paddingTop": 0,
        "paddingRight": 0,
        "paddingBottom": 0,
        "paddingLeft": 0
    },
    "p-5": {
        "paddingTop": 5,
        "paddingRight": 5,
        "paddingBottom": 5,
        "paddingLeft": 5
    },
    "p-10": {
        "paddingTop": 10,
        "paddingRight": 10,
        "paddingBottom": 10,
        "paddingLeft": 10
    },
    "p-15": {
        "paddingTop": 15,
        "paddingRight": 15,
        "paddingBottom": 15,
        "paddingLeft": 15
    },
    "p-20": {
        "paddingTop": 20,
        "paddingRight": 20,
        "paddingBottom": 20,
        "paddingLeft": 20
    },
    "p-r-5": {
        "paddingRight": 5
    },
    "p-l-5": {
        "paddingLeft": 5
    },
    "p-t-5": {
        "paddingTop": 5
    },
    "p-b-5": {
        "paddingBottom": 5
    },
    "p-r-10": {
        "paddingRight": 10
    },
    "p-l-10": {
        "paddingLeft": 10
    },
    "p-t-10": {
        "paddingTop": 10
    },
    "p-b-10": {
        "paddingBottom": 10
    },
    "p-r-15": {
        "paddingRight": 15
    },
    "p-l-15": {
        "paddingLeft": 15
    },
    "p-t-15": {
        "paddingTop": 15
    },
    "p-b-15": {
        "paddingBottom": 15
    },
    "bor-0": {
        "border": 0
    },
    "bora-0": {
        "borderRadius": 0
    },
    "bor-1": {
        "border": "1px solid #e4e2e2"
    },
    "bor-r-20": {
        "borderRadius": 20
    },
    "f-500": {
        "fontWeight": "500"
    },
    "f-600": {
        "fontWeight": "600"
    },
    "f-700": {
        "fontWeight": "700"
    },
    "f-800": {
        "fontWeight": "800"
    },
    "f-900": {
        "fontWeight": "900"
    },
    "fs-16": {
        "fontSize": 16
    },
    "fs-15": {
        "fontSize": 15
    },
    "txt-white": {
        "color": "#FFF"
    },
    "bg-white": {
        "backgroundColor": "#FFFFFF"
    },
    "*": {
        "boxSizing": "border-box"
    },
    "*:before": {
        "boxSizing": "border-box"
    },
    "*:after": {
        "boxSizing": "border-box"
    },
    "chat chat-history": {
        "paddingTop": 30,
        "paddingRight": 30,
        "paddingBottom": 20,
        "paddingLeft": 30,
        "borderBottom": "2px solid white"
    },
    "chat chat-history message-data": {
        "marginBottom": 15
    },
    "chat chat-history message-data-time": {
        "color": "#a8aab1",
        "paddingLeft": 6
    },
    "chat chat-history message": {
        "color": "white",
        "paddingTop": 5,
        "paddingRight": 20,
        "paddingBottom": 5,
        "paddingLeft": 20,
        "lineHeight": 26,
        "fontSize": 15,
        "marginBottom": 5,
        "width": "90%",
        "position": "relative"
    },
    "chat chat-history message-non-content": {
        "color": "white",
        "paddingTop": 5,
        "paddingRight": 20,
        "paddingBottom": 5,
        "paddingLeft": 20,
        "lineHeight": 26,
        "fontSize": 15,
        "marginBottom": 5,
        "width": "90%",
        "position": "relative"
    },
    "chat chat-history message-non-content: after": {
        "position": "absolute",
        "top": -15,
        "left": 5,
        "borderWidth": "0 15px 15px",
        "borderStyle": "solid",
        "borderColor": "#CCDBDC transparent",
        "display": "block",
        "width": 0
    },
    "chat chat-history message:after": {
        "content": "",
        "position": "absolute",
        "top": -15,
        "left": 5,
        "borderWidth": "0 15px 15px",
        "borderStyle": "solid",
        "borderColor": "#CCDBDC transparent",
        "display": "block",
        "width": 0
    },
    "chat chat-history you-message": {
        "background": "#95c809",
        "color": "#fff"
    },
    "chat chat-history you-message:after": {
        "borderColor": "#95c809 transparent"
    },
    "chat chat-history me-message": {
        "background": "#CCDBDC",
        "color": "#003366"
    },
    "chat chat-history me-message:after": {
        "borderColor": "#CCDBDC transparent",
        "right": 5,
        "top": -15,
        "left": "auto",
        "bottom": "auto"
    },
    "chat chat-message": {
        "paddingTop": 30,
        "paddingRight": 30,
        "paddingBottom": 30,
        "paddingLeft": 30
    },
    "chat chat-message fa-file-o": {
        "fontSize": 16,
        "color": "gray",
        "cursor": "pointer"
    },
    "chat chat-message fa-file-image-o": {
        "fontSize": 16,
        "color": "gray",
        "cursor": "pointer"
    },
    "chat-ul li": {
        "listStyleType": "none"
    },
    "align-left": {
        "textAlign": "left"
    },
    "align-right": {
        "textAlign": "right"
    },
    "float-right": {
        "float": "right"
    },
    "clearfix:after": {
        "visibility": "hidden",
        "display": "block",
        "fontSize": 0,
        "content": " ",
        "clear": "both",
        "height": 0
    },
    "you": {
        "color": "#95c809"
    },
    "me": {
        "color": "#CCDBDC"
    },
    "h1": {
        "fontFamily": "\"Raleway\",sans-serif",
        "color": "#003366"
    },
    "h2": {
        "fontFamily": "\"Raleway\",sans-serif",
        "color": "#003366"
    },
    "h3": {
        "fontFamily": "\"Raleway\",sans-serif",
        "color": "#003366"
    },
    "h4": {
        "fontFamily": "\"Raleway\",sans-serif",
        "color": "#003366"
    },
    "h5": {
        "fontFamily": "\"Raleway\",sans-serif",
        "color": "#003366"
    },
    "h6": {
        "fontFamily": "\"Raleway\",sans-serif",
        "color": "#003366"
    },
    "dropbtn": {
        "backgroundColor": "#4CAF50",
        "color": "white",
        "paddingTop": 16,
        "paddingRight": 16,
        "paddingBottom": 16,
        "paddingLeft": 16,
        "fontSize": 16,
        "border": "none",
        "cursor": "pointer"
    },
    "dropdown": {
        "position": "relative",
        "display": "inline-block",
        "cursor": "pointer"
    },
    "dropdown-content": {
        "display": "none",
        "position": "absolute",
        "backgroundColor": "#ededed",
        "color": "#000 !important",
        "minWidth": 50,
        "paddingLeft": 5,
        "paddingRight": 5,
        "boxShadow": "0px 8px 16px 0px rgba(0,0,0,0.2)",
        "zIndex": 9999
    },
    "dropdown-content a": {
        "color": "black",
        "paddingTop": 12,
        "paddingRight": 16,
        "paddingBottom": 12,
        "paddingLeft": 16,
        "textDecoration": "none",
        "display": "block"
    },
    "dropdown-content a:hover": {
        "backgroundColor": "#f1f1f1"
    },
    "dropdown:hover dropdown-content": {
        "display": "block"
    },
    "dropdown:hover dropbtn": {
        "backgroundColor": "#3e8e41"
    },
    "li-active": {
        "cursor": "pointer !important",
        "WebkitBoxShadow": "inset 0px 6px 10px 0px rgba(220, 225, 227, 0.75)!important",
        "MozBoxShadow": "inset 0px 6px 10px 0px rgba(220, 225, 227, 0.75)!important",
        "boxShadow": "inset 0px 6px 10px 0px rgba(220, 225, 227, 0.75)!important",
        "color": "#95c809!important"
    },
    "li-active> div > a": {
        "color": "#95c809!important"
    }
});