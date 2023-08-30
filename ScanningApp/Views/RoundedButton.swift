/*
 Piyush Acharya
 8/29/2023
 @VerisimilitudeX
 */
import UIKit

@IBDesignable
class RoundedButton: UIButton {
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setup()
    }
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setup()
    }
    
    func setup() {
        backgroundColor = .appBlue
        layer.cornerRadius = 8
        clipsToBounds = true
        setTitleColor(.white, for: [])
        titleLabel?.font = UIFont.boldSystemFont(ofSize: 17)
    }
    
    override var isEnabled: Bool {
        didSet {
            backgroundColor = isEnabled ? .appBlue : .appGray
        }
    }
    
    var toggledOn: Bool = true {
        didSet {
            if !isEnabled {
                backgroundColor = .appGray
                return
            }
            backgroundColor = toggledOn ? .appBlue : .appLightBlue
        }
    }
}
