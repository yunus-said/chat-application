import React from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import Hoc from "../hoc/hoc";

class Profile extends React.Component {
  render() {
    if (this.props.token === null) {
      return <Redirect to="/" />;
    }
    console.log('The image', this.props.image);
    return (
      <div className="contact-profile">
        {this.props.username !== null ? (
          <Hoc>
            <img src="admin.jpg" />
            <p>{this.props.username}</p>
            <div className="social-media">
              <i className="fa fa-facebook" aria-hidden="true" />
              <i className="fa fa-twitter" aria-hidden="true" />
              <i className="fa fa-instagram" aria-hidden="true" />
            </div>
          </Hoc>
        ) : null}
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    username: state.auth.username,
    image: state.auth.image,
    token: state.auth.token
  };
};

export default connect(mapStateToProps)(Profile);
