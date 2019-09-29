import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow {
    id: mainWindow
    height: 160
    width: 300
    visible: true
    title: "A title"

    Item {
        id: page
        visible: true
        width: parent.width

        Rectangle {
            height: {
                console.log("I am a comment")
                return 160
            }
            width: 100
            color: "#ff0000"

            Text {
                text: "I am some regular text"
                height: 50
                width: parent.width
                font.pixelSize: 12
            }
        }
    }
}